@echo off
REM JARVIS-XXXIX Launcher for Windows
REM Automatically installs dependencies and starts JARVIS

title JARVIS-XXXIX - Advanced Computer Control AI
echo.
echo Starting JARVIS-XXXIX...
echo.

REM Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python not found. Please install Python 3.9+
    echo Download from: https://www.python.org
    pause
    exit /b 1
)

REM Run setup
python setup.py

REM Run main
echo.
echo Launching JARVIS-XXXIX...
python main.py

pause