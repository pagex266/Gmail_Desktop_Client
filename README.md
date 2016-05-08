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

### Configure Gmail account
You will probably notice that the Gmail application will not initialy allow you to send the your mail. To configure your account to do so please go to: https://www.google.com/settings/security/lesssecureapps and TOGGLE ON to do so.

**_After using the Desktop Client go back to link and TOGGLE OFF to keep your account secure from malicous software_**