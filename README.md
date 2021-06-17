# login-check

Problem : Fingerprint scanner for check In had been deactivated due to Coronavirus. There was no way to track the attendance of the office staff. 

Solution :

A program that sends outlook mail notification when a user has logged into their computer for the first time in the day allowing tracking of time at work. 


1. patch.bat file creates a schedule task to run login_check.exe
2. Schedule task is created by the configuration in the attached login_check.xml file.
3. Executable from python file was created by using PyInstaller and does the following :

  --- copies login_check.exe into the users document folder.

  --- creates schedule task in users pc as per login_check.xml
  
  
  Note: Patch was run on only some IP adresses (6 Desktops connected on the same LAN) to track login time.
  The IP address was discovered by running the program in ip-finder repository. (https://github.com/harshvsthakur/ip-finder)
