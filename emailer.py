import smtplib
import argparse
import base64

sender = 'heather.e.armstrong@gmail.com'
receivers = ['heather.e.armstrong@gmail.com']

almond_file = open('almonds.txt', 'r')

message_template = """From: Heather <heather.e.armstrong@gmail.com>
To: Me <heather.e.armstrong@gmail.com>
Subject: This week's almond situation

Bulk Barn has these almonds in this week's flyer:
%s

Sent to you by PYTHON MAGIC!
"""

almonds = almond_file.read()

message = message_template % almonds

parser = argparse.ArgumentParser()
parser.add_argument('password', action="store")
args = parser.parse_args()

username = 'heather.e.armstrong@gmail.com'
password = base64.b64decode(args.password)

try:
  smtpObj = smtplib.SMTP('smtp.gmail.com:587')
  smtpObj.starttls()
  smtpObj.login(username, password)
  smtpObj.sendmail(sender, receivers, message)
  smtpObj.quit()
except smtplib.SMTPException:
  print "Error: unable to send email"

