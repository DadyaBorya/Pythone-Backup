import os


def creation_date(path):
    return os.path.getmtime(path)
