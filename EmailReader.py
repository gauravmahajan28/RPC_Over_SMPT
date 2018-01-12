import smtplib
import time
import imaplib
import email
import sys


try:
    for line in open("passwords.txt", "r").readlines():  # Read the lines
        login_info = line.split()  # Split on the space, and store the results in a list of two strings
        print(login_info[0])
        print(login_info[1])

    FROM_EMAIL = login_info[0]
    FROM_PWD = login_info[1]
    SMTP_SERVER = "imap.gmail.com"
    SMTP_PORT = 993
    mail = imaplib.IMAP4_SSL(SMTP_SERVER)
    mail.login(FROM_EMAIL, FROM_PWD)
    mail.select('inbox')
    type, data = mail.search(None, 'ALL')
    mail_ids = data[0]
    id_list = mail_ids.split()
    first_email_id = int(id_list[0])
    latest_email_id = int(id_list[-1])
    print("done")
    type, data = mail.fetch(str(latest_email_id), '(RFC822)')
    email_content = data[0][1]
    msg = email.message_from_bytes(email_content)  # this needs to be corrected in your case
    maintype = msg.get_content_maintype()
    print(msg.get_payload())
   # print(msg)
    emailDate = msg["Date"]
    emailSubject = msg["Subject"]
    emailBody = msg["Message"]
  #  print(emailDate)
  #  print(emailSubject)
  #  print(emailBody)



except Exception as ex:
    print(ex)
    print("Unexpected error:", sys.exc_info()[0])
    print("erorr occured")
