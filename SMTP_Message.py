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
myPass = raw_input("Enter your Gmail Password: ")
msg['To'] = raw_input("Enter the email address you wish to send to: ")
msg['Subject'] = raw_input("Enter the subject of your email: ")

# Run the main program
try:
	smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
except:
	print("Cannot make connection to gmail SMTP server on port 587")
	sys.exit()
# Send a basic hello message to the server
smtpObj.ehlo()
# Encrypt the Email. SMTP -> SMTPS
smtpObj.starttls()
# Login
try:
	smtpObj.login(msg['From'], myPass)
except:
	print("Cannot login. Please read README and/or correct username and/or password")
	sys.exit()
# Send the message
try:
	smtpObj.sendmail(msg['From'], msg['To'], msg.as_string())
except:
	print("Cannot Send Message")
	pass
# Close the Connection
smtpObj.close()
