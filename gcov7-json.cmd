@echo off
setlocal

set "mydir=%~dp0"
python3 "%mydir%\gcov7-json.py" %*
