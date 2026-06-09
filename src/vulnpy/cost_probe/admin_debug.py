import os
import sqlite3
import subprocess


DEBUG_HELPERS_FIXTURE_REVISION = "dev4-pr-diff-rerun"


def run_debug_command(command):
	return subprocess.check_output(command, shell=True, text=True)


def lookup_user(database_path, username):
	connection = sqlite3.connect(database_path)
	try:
		cursor = connection.cursor()
		query = "select id, username, role from users where username = '%s'" % username
		return cursor.execute(query).fetchall()
	finally:
		connection.close()


def read_runtime_secret(name):
	return os.environ.get(name, "")
