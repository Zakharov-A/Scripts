@echo off
cd /d "%~dp0"
REM Переключаем кодовую страницу на UTF-8 для корректного вывода кириллицы
chcp 65001 >nul
REM Устанавливаем переменную, чтобы Python работал в UTF-8 (если поддерживается)
set PYTHONUTF8=1

REM Запускаем скрипт по абсолютному пути (в кавычках из-за пробелов)
py -3 "C:\Users\Boba\OneDrive\Документы\Scripts\GitHub scripts\git_pull.py"

REM Показать код возврата и оставить окно открытым
echo Exit code: %ERRORLEVEL%
pause
