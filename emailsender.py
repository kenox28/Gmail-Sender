import smtplib
from email.mime.text import MIMEText
message = MIMEText('send message in python')
message['Subject'] = "blabla"
message['From'] = "iquenxzx@gmail.com" #inputed
message['To'] = "iquenxzx@gmail.com"    #inputed 

sev = smtplib.SMTP("smtp.gmail.com", 587)
sev.starttls()
sev.login("iquenxzx@gmail.com","tpxb aabi milk biym")

sev.send_message(message)
sev.quit()

print("Email sent succesfuly")
