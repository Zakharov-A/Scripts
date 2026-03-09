import subprocess
import sys
import os
from pathlib import Path

def git_pull(cwd=None, timeout=None):
	cwd = Path(cwd) if cwd else Path(os.getcwd())
	try:
		result = subprocess.run(
			["git", "pull"],
			cwd=str(cwd),
			capture_output=True,
			text=True,
			check=False,
			timeout=timeout
		)
	except FileNotFoundError:
		print("Ошибка: git не установлен или найден в PATH.", file=sys.stderr)
		return 2
	except subprocess.TimeoutExpired:
		print(f"Ошибка: команда git pull превысила таймаут {timeout} секунд. ", file=sys.stderr)
		return 3


	if result.stdout:
		print(result.stdout, end="")
	if result.stderr:
		print(result.stderr, file=sys.stderr, end="")

	
	return result.returncode


if __name__ == "__main__":
	timeout_env = os.environ.get("GIT_PULL_TIMEOUT")
	timeout = int(timeout_env) if timeout_env and timeout_env.isdigit() else None

	code = git_pull(timeout=timeout)
	if code == 0:
		print("\nGit pull выполнен успешно.")
	else:
		print(f"\nGit pull завершился с кодом {code}.", file=sys.stderr)
	sys.exit(code)	












