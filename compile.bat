@echo off
title Compile
rem --enable-plugin=numpy
rem set /P file="which file would you like to compile? "
py -m nuitka easm.py --standalone --onefile --enable-plugin=tk-inter

pause