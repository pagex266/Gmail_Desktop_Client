'''
Name: Grant Page
CS 5651 Final Project
Date: Wednessday, May 4 2016
'''

# add import
import smtplib
from email.mime.text import MIMEText

# Load values
f = open('message.txt', 'r')
msg = MIMEText(f.read())
msg['From'] = raw_input("Enter your Gmail UserName: ")
msg['From'] = msg['From'] + "@gmail.com"
myPass = raw_input("Enter your Gmail Password: ")
msg['To'] = raw_input("Enter the email address you wish to send to: ")
msg['Subject'] = raw_input("Enter the subject of your email: ")

# Run the main program
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(msg['From'], myPass)
smtpObj.sendmail(msg['From'], msg['To'], msg.as_string())
smtpObj.close()
