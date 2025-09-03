import smtplib
import ssl
from email.message import EmailMessage

# Your email and app password
sender_email = "priyamsanodiya340@gmail.com"
password = ""   # NOT your Gmail login password

# Receiver
receiver_email = "priyamsanodiya77@gmail.com"

# Create email
msg = EmailMessage()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "Hello from Python"
msg.set_content("This is a simple test email sent using Python ✅")

# Connect to Gmail SMTP server (SSL on port 465)
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(sender_email, password)
    smtp.send_message(msg)

print("Email sent successfully ✅")
