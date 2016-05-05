'''
Name: Grant Page
CS 5651 Final Project
Date: Wednessday, May 4th 2016
'''

# Import Python Packages
import imapclient

# Initialize variables
UserName = raw_input("Enter your Gmail UserName: ")
UserName = UserName + "@gmail.com"
Password = raw_input("Enter your Gmail Password: ")

# Set up a imapObj
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
# Loggin into the IMAP Server
imapObj.login(UserName, Password)
# Selecting a Folder
imapObj.select_folder('INBOX', readonly=True)

