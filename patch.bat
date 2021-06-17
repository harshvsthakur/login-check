@echo off 

SET mypath=%~dp0
SET topath=C:\Users\%USERNAME%\Documents
SET xmlpath=%mypath%login_check.xml

robocopy %mypath% %topath% login_check.exe

schtasks /Create /TN "login_check" /XML %xmlpath%