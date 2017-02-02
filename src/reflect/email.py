from background_task import background
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.conf import settings

def notify_email(email,question):
    # sent user we had received their submission
	plain_reply = '關於您先前詢問的問題:\n'+question+'學聯會福利部將會儘快處理\n'
	html_design = """<html><head><meta charset="UTF-8"><link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet"><title>Simple, flat contact form</title></head><body style="background-color: #f6f6f6;"><section class="container" style="font-family: \'Open Sans\', sans-serif;position: relative;text-align: center;background: white;padding: 13px;height: 300px;width: 80%;margin: 20px auto 5px auto;"><section class="header" style="font-family: \'Open Sans\', sans-serif;position: relative;text-align: left;font-size: 150%;margin: 5px 10% 0 10%;"><p>關於您先前詢問的 : """ + question + """</p><p>學聯會福利部已經收到您的信件了，並且將會在看到信件後作出答覆 </p></section></body></html>"""
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "收到關於您的問題"
	msg['From'] = "welfare.stu.nctu@gmail.com"
	msg['To'] = email
	part1 = MIMEText(plain_reply, 'plain')
	part2 = MIMEText(html_design, 'html')
	msg.attach(part1)
	msg.attach(part2)

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(settings.EMAIL_ID, settings.EMAIL_KEY)
	server.sendmail(settings.EMAIL_ID, email, msg.as_string())
	server.quit()

def send_reply(subject,email,content):
    # lookup user by email and send them a message
	plain_reply = '關於您先前詢問的問題:\n'+subject+'學聯會福利部的答覆如下:\n'+content
	html_design = """<html><head><meta charset="UTF-8"><link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet"><title>Simple, flat contact form</title></head><body style="background-color: #f6f6f6;"><section class="container" style="font-family: \'Open Sans\', sans-serif;position: relative;text-align: center;background: white;padding: 13px;height: 300px;width: 80%;margin: 20px auto 5px auto;"><section class="header" style="font-family: \'Open Sans\', sans-serif;position: relative;text-align: left;font-size: 150%;margin: 5px 10% 0 10%;"><p>關於您先前詢問的 : """ + subject + """</p><p>學聯會福利部給出的答覆如下    : </p></section><p class="content" style="font-size: 120%;color: #353535;"> """+content+"""</p></section></body></html>"""
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "回覆：關於您的"+subject
	msg['From'] = "welfare.stu.nctu@gmail.com"
	msg['To'] = email
	part1 = MIMEText(plain_reply, 'plain')
	part2 = MIMEText(html_design, 'html')
	msg.attach(part1)
	msg.attach(part2)

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(settings.EMAIL_ID, settings.EMAIL_KEY)
	server.sendmail(settings.EMAIL_ID, email, msg.as_string())
	server.quit()