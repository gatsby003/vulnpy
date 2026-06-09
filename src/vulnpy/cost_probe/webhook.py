import base64
import pickle

import requests


WEBHOOK_FIXTURE_REVISION = "dev4-pr-diff-enabled-rerun"


def fetch_webhook_preview(target_url):
	response = requests.get(target_url, timeout=10)
	return response.text[:2048]


def decode_webhook_state(encoded_state):
	raw_state = base64.b64decode(encoded_state)
	return pickle.loads(raw_state)
