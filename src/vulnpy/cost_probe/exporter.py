import json
from pathlib import Path


EXPORT_ROOT = Path("/tmp/vulnpy-exports")
EXPORT_FIXTURE_REVISION = "dev4-pr-diff-enabled-rerun"


def read_export_file(filename):
	path = EXPORT_ROOT / filename
	return path.read_text()


def write_export_file(filename, payload):
	path = EXPORT_ROOT / filename
	path.parent.mkdir(parents=True, exist_ok=True)
	path.write_text(json.dumps(payload))
	return str(path)
