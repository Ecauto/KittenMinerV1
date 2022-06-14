:top
@echo off
title Kitten Miner Project Home (By Izikut)
mode con lines=27 cols=122


echo.
echo [1] Start Script
echo [2] Install Modules
echo [3] Clear Wallet
echo [4] Send All Crypto
echo [5] Credit
echo.
set /p Q= 

if %Q%==1 (
Start Kitten.pyw
goto top
)

if %Q%==2 (
pip install bitcoin
pip install pyarmor
pip install colorama
pip install requests
pip install pystyle
pip install PySimpleGUI
goto top
)

if %Q%==3 (
echo Soon..
pause
goto top
)

if %Q%==4 (
echo Soon..
pause
goto top
)

if %Q%==5 (
echo Izikut
pause
goto top
)




























































if %Q%==admin (
Echo Soon
timeout 1
goto top
)










