from csv_parse.reader import parse


def test_simple_quotes():
    data = memoryview(b'"foo","bar"\n"baz","bat"')
    size = len(data)
    result = parse(data, size, quote='"')
    assert result == [("foo", "bar"), ("baz", "bat")]


def test_simple_quotes_with_separator():
    data = memoryview(b'"foo,oof","bar"\n"baz","bat"')
    size = len(data)
    result = parse(data, size, quote='"')
    assert result == [("foo,oof", "bar"), ("baz", "bat")]


def test_simple_quotes_with_newline():
    data = memoryview(b'"foo\noof","bar"\n"baz","bat"')
    size = len(data)
    result = parse(data, size, quote='"')
    assert result == [("foo\noof", "bar"), ("baz", "bat")]
