@echo off
echo Checking for Windows updates...
powershell -Command "Get-WindowsUpdateLog"
pause

:: Check for Windows updates and display the update log

