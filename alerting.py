import os
import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import subprocess
import sys

hostname = os.popen('cat /etc/hostname').read()

#récupère seulement l'ip
cmd_get_ip= "ip a | grep 172.29 | awk '{print $2}'"
ip = subprocess.popen(cmd_get_ip, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
output = ip.communicate()[0]

msg=MIMEMultipart()
msg['From']= "sender"
msg['To']= "target"
msg['Subject'] ="Alert on honeypot" + hostname +" at IP " + output

body=open('/opt/dionaea/var/log/dionaea/50lastlines', 'r')
body = MIMEText(body.read())
msg.attach(body)

server = smtplib.SMTP('smtp_ip', 25)

server.ehlo()
server.set_debuglevel(2)
server.sendmail('sender@test.com', 'target@test.com', msg.as_string())
server.quit
