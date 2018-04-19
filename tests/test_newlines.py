from csv_parse.reader import parse


def test_simple_multiline_parse():
    data = memoryview('foo,bar\nbaz,bat')
    size = len(data)
    result = parse(data, size)
    assert result == [("foo", "bar"), ("baz", "bat")]


def test_simple_quoted_multiline_parse():
    data = memoryview('"fo\no","bar"\n"baz","bat"')
    size = len(data)
    result = parse(data, size, quote='"')
    assert result == [("fo\no", "bar"), ("baz", "bat")]


def test_simple_escaped_multiline_parse():
    data = memoryview('''fo\
o,bar\nbaz,bat''')
    size = len(data)
    result = parse(data, size)
    assert result == [("fo\no", "bar"), ("baz", "bat")]
