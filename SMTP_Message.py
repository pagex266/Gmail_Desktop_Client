#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
'''
Name: Grant Page
CS 5651 Final Project
Date: Wednessday, May 4 2016
'''

# add import
import smtplib
import sys
from email.mime.text import MIMEText

# Load values
f = open('message.txt', 'r')
msg = MIMEText(f.read())
msg['From'] = raw_input("Enter your Gmail UserName: ")
msg['From'] = msg['From'] + "@gmail.com"
myPass = raw_input("Enter your Password (generated in App passwords): ")
msg['To'] = raw_input("Enter the email address you wish to send to: ")
msg['Subject'] = raw_input("Enter the subject of your email: ")

# Run the main program
try:
	smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
except:
	print("Cannot make connection to gmail SMTP server on port 587")
	sys.exit()

# Make a connection with the server
try:
	smtpObj.ehlo()
except:
	print("SMTP Server is not responding.\nTry annother time.")
	sys.exit()

# Login
try:
	smtpObj.login(msg['From'], myPass)
except:
	print("Incorrect username or password.\nMake sure you are using 2-Step Verification (see README for more info)")
	sys.exit()

# Send the message
try:
	smtpObj.sendmail(msg['From'], msg['To'], msg.as_string())
except:
	print("Cannot Send Message")
	pass
# Close the Connection
smtpObj.close()
