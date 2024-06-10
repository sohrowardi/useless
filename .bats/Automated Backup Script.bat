@echo off
set SOURCE="C:\Users\YourUsername\Documents"
set DEST="D:\Backup\Documents"
xcopy %SOURCE% %DEST% /E /H /C /I /Y
echo Backup completed successfully!
pause

:: Automatically back up important files and directories to a specified backup location
