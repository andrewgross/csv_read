from tests.helpers import get_file_path
from csv_parse.reader import parse, read


def test_simple_multiline_parse():
    data = memoryview(b'foo,bar\nbaz,bat')
    size = len(data)
    result = parse(data, size)
    assert result == [("foo", "bar"), ("baz", "bat")]


def test_simple_quoted_multiline_parse():
    data = memoryview(b'"fo\no","bar"\n"baz","bat"')
    size = len(data)
    result = parse(data, size, quote='"')
    assert result == [("fo\no", "bar"), ("baz", "bat")]


def test_simple_escaped_multiline_parse():
    path = get_file_path("escape_newline")
    result = read(path)
    assert result == [("fo\no", "bar"), ("baz", "bat")]
