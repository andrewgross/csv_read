from tests.helpers import get_file_path
from csv_parse.reader import read


def test_simple_quote_escape():
    path = get_file_path("escape_quote")
    result = read(path, quote='"')
    assert result == [('foo"oo', "bar"), ("baz", "bat")]


def test_double_escape():
    path = get_file_path("escape_escape")
    result = read(path, quote='"')
    assert result == [('fo\\o', "bar"), ("baz", "bat")]
