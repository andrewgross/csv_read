import os
from StringIO import StringIO


def read(filename, field_separator=',', null_as=""):
    size = os.path.getsize(filename)
    with open(filename, 'rb') as f:
        data = memoryarray(f.read())
    return parse(data, size, field_separator=field_separator, null_as=null_as)


def parse(data, size, field_separator, null_as="")
    parsed_data = []
    row_data = []
    field_data = bytearray()
    i = 0
    while i < size:
        byte = data[i]



        i = i + 1

# Ensure we are still in bounds
# If we are "escaped"
    # Unset "escaped", append and move on


# Check if we are a field delimiter
    # Take our current buffer, finish it
    # Add it to row data
# Check if we are a newline character

# What about quoted fields?
