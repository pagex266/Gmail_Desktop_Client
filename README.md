# Gmail_Desktop_Client
Very basic Gmail Desktop client. Can only send mail through SMTP and recieve mail through IMAP

## SMTP_Message.py
This python script is used to send a message from an existing GMAIL account using SMTP protocol on google's mail server. user provides gmail username, password, and the email address of the person you want to send to.

## get_IMAP.py
This python script is used to gather an exiting gmail user's INBOX data and store it within the file INBOX.txt for refrence. By providing the email's UID the user is able to look at the text of an email.

## The Followng resources must be provided by the user
1. Must have a download of Python 2.7
2. Must have the 'smtplib' libary avalible
3. Must have installed imapclient -> 'pip install imapclient'
4. Must have installed pyzmail -> 'pip install pyzmail'

### Text Content
The Content of the file message.txt will be the body of the Email message you wish to send through SMTP_Message.py

### INBOX cache
the file INBOX.txt will be generated whenever you run get_IMAP.py, This file is the result of iterating through the your gmail INBOX and appendnding the results to a file. The file is ordered from least recent at the top to most recent at the bottom

### Set up 2-Step Verification
This application requires you enable Two-Factor-Authentication.
Visit: https://myaccount.google.com/security and enable 2-Step Verification.

### Add Password for application
To connect to the application you will need to add a password. https://security.google.com/settings/security/apppasswords Under The first category select 'custom' and then click 'generated'. The generated password will be your password for your gmail account for these programs.
