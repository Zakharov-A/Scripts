import os
from datetime import datetime


def run(cmd):
    print(f"\n>>> {cmd}")
    rc = os.system(cmd)
    return rc


def main():
    cwd = os.getcwd()
    print("Working dir:", cwd)

    # 1. git status
    rc = run("git status")
    if rc != 0:
        print("Ошибка: git status завершился с ошибкой.")
        os._exit(rc)

    # 2. git add .
    rc = run("git add .")
    if rc != 0:
        print("Ошибка: git add завершился с ошибкой.")
        os._exit(rc)

    # 3. git commit -m "date"
    msg = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    rc = run(f'git commit -m "{msg}"')

    # Если нечего коммитить - git commit вернёт код 1, это нормально
    if rc not in (0, 1):
        print("Ошибка: git commit завершился с ошибкой.")
        os._exit(rc)

    # 4. git push
    rc = run("git push")
    if rc == 0:
        print("\nGit push выполнен успешно.")
    else:
        print("\nGit push завершился с ошибкой.")

    os._exit(rc)

if __name__ == "__main__":
    main()

    





