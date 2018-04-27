PACKAGE=csvparse
CUSTOM_PIP_INDEX=pypi


all: setup test

prepare: clean install_deps

setup: prepare

pre_commit: setup
	@pre-commit run --all-files

test:
	@py.test --cov=csv_parse tests/

clean:
	@rm -rf .cache
	@rm -rf build/
	@rm -f .build.log
	@rm -rf .pytest_cache/
	@echo "Removing garbage..."
	@find . -name '*.pyc' -delete
	@find . -name '*.so' -delete
	@find . -name __pycache__ -delete
	@rm -rf .coverage *.egg-info *.log build dist MANIFEST yc

install_deps:
	@if [ -z $$VIRTUAL_ENV ]; then \
		echo "===================================================="; \
		echo "You're not running this from a virtualenv, wtf?"; \
		echo "ಠ_ಠ"; \
		echo "===================================================="; \
		exit 1; \
	fi

	@if [ -z $$SKIP_DEPS ]; then \
		echo "Installing missing dependencies..."; \
		[ -e development.txt  ] && pip install --quiet -r development.txt; \
	fi
	@pre-commit install
	@python setup.py develop &> .build.log


publish: clean tag
	@if [ -e "$$HOME/.pypirc" ]; then \
		echo "Uploading to '$(CUSTOM_PIP_INDEX)'"; \
		python setup.py sdist bdist_wheel; \
		python3 setup.py bdist_wheel; \
		twine upload dist/*; \
	else \
		echo "You should create a file called '.pypirc' under your home dir.\n"; \
		echo "That's the right place to configure 'pypi' repos.\n"; \
		exit 1; \
	fi

tag:
	@if [ $$(git rev-list $$(git describe --abbrev=0 --tags)..HEAD --count) -gt 0 ]; then \
		if [ $$(git log  -n 1 --oneline $$(git describe --abbrev=0 --tags)..HEAD CHANGELOG.md | wc -l) -gt 0 ]; then \
			git tag $$(python setup.py --version) && git push --tags || echo 'Version already released, update your version!'; \
		else \
			echo "CHANGELOG not updated since last release!"; \
			exit 1; \
		fi; \
	else \
		echo "No commits since last release!"; \
		exit 1;\
	fi
