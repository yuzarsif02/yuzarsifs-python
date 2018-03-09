# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib
 
# creates SMTP session
s=smtplib.SMTP("smtp.gmail.com", 587)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login("yusufhvr@gmail.com","*****")

# message to be sent
message = "hii machii"
 
# sending the mail
s.sendmail("yusufhvr@gmail.com","yusufhvr@gmail.com",message)
 
# terminating the session
s.quit()
