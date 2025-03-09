@echo off
setlocal
REM Activate the virtual environment
call C:\Users\pc\Desktop\fish_dealer_software\venv\Scripts\activate.bat

REM Now run your Python script using the virtual environment's Python
"C:\Users\pc\Desktop\fish_dealer_software\python\python.exe" "C:\Users\pc\Desktop\fish_dealer_software\app\main.py"

REM Pause to keep the command window open
pause
