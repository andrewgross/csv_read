from csv_parse.reader import parse


def test_simple_parse():
    data = memoryview('foo,bar')
    size = len(data)
    result = parse(data, size)
    assert result == [("foo", "bar")]
