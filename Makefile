all: test


test:
	@py.test --cov=csv_parse tests/


setup:
	@pip install --quiet -r development.txt
