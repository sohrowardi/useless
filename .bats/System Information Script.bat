@echo off
echo System Information
echo ===================
systeminfo | findstr /C:"OS Name" /C:"OS Version" /C:"System Manufacturer" /C:"System Model" /C:"Total Physical Memory"
pause

:: Display basic system information such as OS name, version, manufacturer, model, and total physical memory.