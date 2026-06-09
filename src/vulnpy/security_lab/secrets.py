import os


def read_named_secret(name):
    return os.environ.get(name, "")


def dump_selected_env(prefix):
    return {
        key: value
        for key, value in os.environ.items()
        if key.startswith(prefix)
    }
