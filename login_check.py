# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 10:03:59 2020

@author: harshvardhans
"""

import win32com.client as win32
import datetime

date = str(datetime.date.today())
time = str(datetime.datetime.now().time())

def mail():
    '''Opens outlook and creates and sends mail'''
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = '' # mail address
    mail.Subject = 'User Log In - ' + time
    mail.HTMLBody = 'User Log In - ' + time
    mail.Send()


def check_send():
    '''checks weather the log in info mail has already been sent.
       If it is not in sent items, the program is terminated'''
    outlook = win32.Dispatch('outlook.application').GetNamespace("MAPI")
    sent = outlook.GetDefaultFolder(5)
    messages = sent.Items
    last_date = str(messages.GetLast().SentOn)
    if date in last_date:
        raise SystemExit
        
    for i in range (0,50):
        prev_date = str(messages.GetPrevious().SentOn)
        subjects = messages.GetPrevious().Subject
        if date in prev_date and 'User Log In' in subjects:
            raise SystemExit
    
    mail()

check_send()
