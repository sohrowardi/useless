@echo off
echo Testing internet speed...
powershell -Command "& {Invoke-WebRequest -Uri https://www.speedtest.net/api/js/speedtest-config.php}"
pause

:: Perform a basic internet speed test using PowerShell and Speedtest.net.