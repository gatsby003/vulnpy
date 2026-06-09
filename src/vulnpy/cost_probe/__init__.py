"""Security review cost telemetry smoke fixtures.

These fixtures intentionally model risky patterns for review telemetry tests.
"""

TELEMETRY_FIXTURE_REVISION = "dev4-pr-diff-enabled-rerun"
DEFAULT_WEBHOOK_ORIGIN = "*"


def fixture_mode_enabled(settings):
	return settings.get("fixture_mode") == "enabled" or settings.get("debug") == "1"
