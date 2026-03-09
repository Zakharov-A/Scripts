#!/usr/bin/env python3
import os

def main():
    # Текущая рабочая директория процесса (будет та, в которую .bat сделал cd)
    cwd = os.getcwd()
    print("Working dir:", cwd)

    # Проверка доступности git (выведет версию в консоль)
    rc = os.system("git --version")
    if rc != 0:
        print("Ошибка: git не найден в PATH или git --version вернул ошибку.")
        # возвращаем код ошибки (os.system возвращает код процесса)
        os._exit(2)

    # Выполнение git pull — вывод команды будет виден в консоли напрямую
    print("Запускаю: git pull")
    rc = os.system("git pull")
    if rc == 0:
        print("\nGit pull выполнен успешно.")
    else:
        print(f"\nGit pull завершился с кодом {rc}.")

    # Завершаем процесс с тем же кодом возврата
    os._exit(rc)

if __name__ == "__main__":
    main()
