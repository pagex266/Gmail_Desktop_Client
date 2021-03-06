#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python
'''
Name: Grant Page
CS 5651 Final Project
Date: Wednessday, May 4th 2016
'''

# Add Imports
import imaplib
import imapclient
import pyzmail
import os
import sys

def Get_Messages(imapObj, UID_dict):
	# Place a size limit
	imaplib._MAXLINE_ = 10000000

	# Begin search
	UIDs = imapObj.search(['ALL'])

	if (os.path.isfile('INBOX.txt')):
		os.remove('INBOX.txt')

	f = open('INBOX.txt', 'w')

	rawMessages = imapObj.fetch(UIDs, ['BODY[]'])

	print("\nLoading...")
	# List the list each UID along with it's subject and sender
	for UID in UIDs:
		try:
			message = pyzmail.PyzMessage.factory(rawMessages[UID]['BODY[]'])
			f.write("UID -> " + str(UID) + "\n")
			f.write("Subject -> " + str(message.get_subject()) + "\n")
			f.write("From -> " + str(message.get_address('from')) + "\n\n")
			UID_dict[UID] = message
		except:
			pass

	f.close()
	print("Open another shell script and see the file INBOX.txt for details on all of you emails")

def View_Message(Message):
	if Message.text_part != None:
		print(Message.text_part.get_payload().decode(Message.text_part.charset))
	elif Message.html_part != None:
		print(Message.html_part.get_payload().decode(Message.html_part.charset))
	else:
		print("ERROR: Cannot print message in text fromat or html format")

# Initialize variables
UserName = raw_input("Enter your Gmail UserName: ")
UserName = UserName + "@gmail.com"
Password = raw_input("Enter your Gmail Password: ")

# Set up a imapObj
try:
	imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
except:
	print("Cannot connect to imap.gmail.com, try again later")
	sys.exit()

# Loggin into the IMAP Server
try:
	imapObj.login(UserName, Password)
except:
	print("UserName or Password Incorrect.\nMake sure you are using 2-Step Verification (see README for more info).")

# Selecting a Folder
imapObj.select_folder('INBOX', readonly=True)

# Initialize the dictionary
UID_DICT = dict()

# Set a boolean to true to keep querying over the list
veiwing = True

# Begin the search
MyMessage = Get_Messages(imapObj, UID_DICT)

while veiwing:
	# Ask the user for the UID
	uid = raw_input("Enter the UID of the file you wish to view: ")
	# Display the chosen message
	try:
		View_Message(UID_DICT[int(uid)])
	except:
		print("INVALID Data")
		pass

	# Ask the user if they wish to do another search
	answer = raw_input("View another message?(y/n): ")
	if (answer != 'Y' or answer != 'y'):
		veiwing = False

# Close the connection
imapObj.logout()
