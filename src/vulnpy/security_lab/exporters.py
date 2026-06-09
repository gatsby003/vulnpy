import csv
import json
from pathlib import Path


EXPORT_ROOT = Path("/tmp/vulnpy-security-lab")


def export_user_report(filename, rows):
    output_path = EXPORT_ROOT / filename
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=["id", "email", "role"])
        writer.writeheader()
        writer.writerows(rows)
    return str(output_path)


def export_raw_json(filename, payload):
    output_path = EXPORT_ROOT / filename
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload))
    return str(output_path)
