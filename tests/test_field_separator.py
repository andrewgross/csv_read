from csv_parse.reader import parse


def test_simple_field_separator():
    data = memoryview(b'foo|bar\nbaz|bat')
    size = len(data)
    result = parse(data, size, field_separator='|')
    assert result == [("foo", "bar"), ("baz", "bat")]


def test_simple_escaped_separator():
    data = memoryview(b'fo\|o|bar\nbaz|bat')
    size = len(data)
    result = parse(data, size, field_separator='|')
    assert result == [("fo|o", "bar"), ("baz", "bat")]


def test_simple_quoted_separator():
    data = memoryview(b'"fo|o"|"bar"\n"baz"|"bat"')
    size = len(data)
    result = parse(data, size, field_separator='|', quote='"')
    assert result == [("fo|o", "bar"), ("baz", "bat")]
