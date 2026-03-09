@echo off
cd /d "%~dp0"
chcp 65001 >nul
set PYTHONUTF8=1

python "C:\Users\Boba\Documents\GitHub\Projects\Scripts\GitHub scripts\git_push.py"

echo Exit code: %ERRORLEVEL%
pause
