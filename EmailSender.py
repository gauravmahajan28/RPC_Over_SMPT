import smtplib
import sys

try:

    for line in open("passwords.txt", "r").readlines():  # Read the lines
        login_info = line.split()  # Split on the space, and store the results in a list of two strings
        print(login_info[0])
        print(login_info[1])
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(login_info[0], login_info[1])
    msg = "Hello"

    SUBJECT = "RPC_SMPT"
    TEXT = "Hello"
    TO = login_info[0]
    gmail_user = login_info[0]

    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % gmail_user,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])
    server.sendmail(gmail_user, TO, BODY)
    print("email sent")
    server.quit()
except:
    print("Unexpected error:", sys.exc_info()[0])
    print("erorr occured")