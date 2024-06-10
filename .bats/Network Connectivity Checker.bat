@echo off
set SERVER=google.com
ping %SERVER% > C:\Users\YourUsername\Desktop\PingLog.txt
echo Ping results logged to PingLog.txt
pause


:: Check if you can reach a specified server and log the results.