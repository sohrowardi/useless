@echo off
echo Displaying saved Wi-Fi passwords...
netsh wlan show profiles
echo.
set /p profile="Enter the Wi-Fi profile name: "
netsh wlan show profile name="%profile%" key=clear | findstr Key
pause

:: Display the saved Wi-Fi passwords on your computer.