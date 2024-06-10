@echo off
set /p time=Enter time in seconds before shutdown: 
shutdown -s -t %time%
echo Your computer will shut down in %time% seconds.
pause

:: Schedule a shutdown after a specified number of seconds