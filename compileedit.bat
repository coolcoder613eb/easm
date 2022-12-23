@echo off
title Compile
rem --windows-disable-console
rem set /P file="which file would you like to compile? "
py -m nuitka "Easm Editor.py" --standalone --onefile --enable-plugin=tk-inter --windows-icon-from-ico=icon.ico
rem pyinstaller -w -i icon.ico -F "Easm Editor.py"

pause