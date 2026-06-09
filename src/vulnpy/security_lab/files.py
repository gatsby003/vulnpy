from pathlib import Path


BASE_DIR = Path("/tmp/vulnpy-security-lab")


def read_named_file(name):
    return (BASE_DIR / name).read_text()


def write_named_file(name, value):
    path = BASE_DIR / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value)
    return str(path)


def read_absolute_path(path):
    return Path(path).read_text()
