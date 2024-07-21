@echo off
:: Set the path for the log file
set LOG_FILE=C:\japhe\latvian-arbitrage\server\arbitrage.log
echo [%date% %time%] Looking for arbitrages... >> %LOG_FILE%

:loop
echo [%date% %time%] Running script... >> %LOG_FILE%
python manage.py calculate_arbitrage >> %LOG_FILE% 2>&1
goto loop