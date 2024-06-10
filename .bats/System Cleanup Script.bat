@echo off
echo Cleaning up temporary files...
del /s /q %temp%\*
rd /s /q %temp%
mkdir %temp%
echo Temporary files cleaned!
pause

:: Clean up temporary files and free up disk space