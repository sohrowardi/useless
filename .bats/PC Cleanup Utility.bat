@echo off
title PC Cleanup Utility

:menu
cls
echo --------------------------------------------------------------------------------
echo PC Cleanup Utility
echo --------------------------------------------------------------------------------
echo.
echo Select a tool
echo =============
echo.
echo [1] Delete Internet Cookies
echo [2] Delete Temporary Internet Files
echo [3] Disk Cleanup
echo [4] Disk Defragment
echo [5] Exit
echo.
set /p op=Run:
if %op%==1 goto delete_cookies
if %op%==2 goto delete_temp_files
if %op%==3 goto disk_cleanup
if %op%==4 goto disk_defrag
if %op%==5 goto exit
goto error

:delete_cookies
cls
echo --------------------------------------------------------------------------------
echo Delete Internet Cookies
echo --------------------------------------------------------------------------------
echo.
echo Deleting Cookies...
ping localhost -n 3 >nul
del /f /q "%userprofile%\AppData\Local\Microsoft\Windows\INetCookies\*.*" >nul 2>&1
cls
echo --------------------------------------------------------------------------------
echo Delete Internet Cookies
echo --------------------------------------------------------------------------------
echo.
echo Cookies deleted.
echo.
echo Press any key to return to the menu. . .
pause >nul
goto menu

:delete_temp_files
cls
echo --------------------------------------------------------------------------------
echo Delete Temporary Internet Files
echo --------------------------------------------------------------------------------
echo.
echo Deleting Temporary Files...
ping localhost -n 3 >nul
del /f /q "%userprofile%\AppData\Local\Microsoft\Windows\Temporary Internet Files\*.*" >nul 2>&1
cls
echo --------------------------------------------------------------------------------
echo Delete Temporary Internet Files
echo --------------------------------------------------------------------------------
echo.
echo Temporary Internet Files deleted.
echo.
echo Press any key to return to the menu. . .
pause >nul
goto menu

:disk_cleanup
cls
echo --------------------------------------------------------------------------------
echo Disk Cleanup
echo --------------------------------------------------------------------------------
echo.
echo Running Disk Cleanup...
ping localhost -n 3 >nul
if exist "C:\WINDOWS\temp" del /f /q "C:\WINDOWS\temp\*.*" >nul 2>&1
if exist "C:\WINDOWS\tmp" del /f /q "C:\WINDOWS\tmp\*.*" >nul 2>&1
if exist "C:\tmp" del /f /q "C:\tmp\*.*" >nul 2>&1
if exist "C:\temp" del /f /q "C:\temp\*.*" >nul 2>&1
if exist "%temp%" del /f /q "%temp%\*.*" >nul 2>&1
if exist "%tmp%" del /f /q "%tmp%\*.*" >nul 2>&1
cls
echo --------------------------------------------------------------------------------
echo Disk Cleanup
echo --------------------------------------------------------------------------------
echo.
echo Disk Cleanup successful!
echo.
pause
goto menu

:disk_defrag
cls
echo --------------------------------------------------------------------------------
echo Disk Defragment
echo --------------------------------------------------------------------------------
echo.
echo Defragmenting hard disks...
ping localhost -n 3 >nul
defrag -c -v
cls
echo --------------------------------------------------------------------------------
echo Disk Defragment
echo --------------------------------------------------------------------------------
echo.
echo Disk Defrag successful!
echo.
pause
goto menu

:error
cls
echo Command not recognized.
ping localhost -n 4 >nul
goto menu

:exit
echo Thanks for using PC Cleanup Utility
ping 127.0.0.1 >nul
exit
