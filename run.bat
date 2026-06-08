@echo off
title 400m Sprint AI Predictor - Setup and Launch
echo ==============================================
echo STARTUJEM DEBUG REZIM APLIKACIE
echo ==============================================

:: Nastavenie priečinka
cd /d "%~dp0"

:: Kontrola Pythonu
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo [CHYBA] Python nie je nainstalovany alebo nie je v PATH.
    pause
    exit /b
)

:: Virtual environment
IF NOT EXIST venv (
    echo [INFO] Vytvaram virtualne prostredie...
    python -m venv venv
)

:: Aktivacia
echo [INFO] Aktivujem prostredie...
call venv\Scripts\activate.bat

:: Instalacia balikov
echo [INFO] Instalujem moduly...
pip install -r requirements.txt --no-cache-dir
IF %ERRORLEVEL% NEQ 0 (
    echo [CHYBA] Problem pri instalacii kniznic.
    pause
    exit /b
)

:: Spustenie Flask servera v novom okne
echo [INFO] Spustam Flask server...
start "Flask Server" cmd /k venv\Scripts\python.exe app.py

:: Cakanie kym server nabehne
timeout /t 5 >nul

:: Otvorenie prehliadaca
echo [INFO] Otvaram prehliadac...
start http://127.0.0.1:5000

echo.
echo Ak sa stranka neotvorila, chod manualne na:
echo http://127.0.0.1:5000
pause