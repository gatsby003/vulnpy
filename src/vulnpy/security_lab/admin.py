import os
import subprocess


def run_maintenance_command(command, cwd=None):
    env = dict(os.environ)
    env["VULNPY_SECURITY_LAB"] = "enabled"
    return subprocess.check_output(
        command,
        cwd=cwd,
        env=env,
        shell=True,
        text=True,
    )


def load_admin_plugin(source):
    namespace = {"__builtins__": __builtins__}
    exec(source, namespace)
    return namespace
