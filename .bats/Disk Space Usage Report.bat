@echo off
echo Disk Space Usage Report
echo =======================
wmic logicaldisk get size,freespace,caption
pause


