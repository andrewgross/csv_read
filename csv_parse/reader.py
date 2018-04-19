import os
from StringIO import StringIO


def read(filename, field_separator=',', null_as=""):
    size = os.path.getsize(filename)
    with open(filename, 'rb') as f:
        data = memoryview(f.read())
    return parse(data, size, field_separator=field_separator, null_as=null_as)


def parse(data, size, field_separator=',', null_as="", newline="\n"):
    parsed_data = []
    row_data = []
    field_data = bytearray()
    i = 0
    while i < size:
        byte = data[i]
        if byte == field_separator:
            row_data.append(field_data)
            field_data = bytearray()
        elif byte == newline:
            row_data.append(field_data)
            field_data = bytearray()
            parsed_data.append(tuple(row_data))
            row_data = []
        else:
            field_data.append(byte)
        i = i + 1
    row_data.append(field_data)
    parsed_data.append(tuple(row_data))
    return parsed_data

# Ensure we are still in bounds
# If we are "escaped"
    # Unset "escaped", append and move on


# Check if we are a field delimiter
    # Take our current buffer, finish it
    # Add it to row data
# Check if we are a newline character

# What about quoted fields?
