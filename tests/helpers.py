import os


def get_file_path(name):
    path = os.path.join("files", "{}.csv".format(name))
    dirname = os.path.dirname(__file__)
    return os.path.join(dirname, path)
