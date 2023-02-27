import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# Set up the sender's email address and login credentials
sender_email = "your.email@gmail.com"
sender_password = "yourpassword"

# Set up the recipient's email address and the email message
recipient_email = "recipient.email@gmail.com"
message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = "Automated Email"

# Attach an image to the email (optional)
with open('image.png', 'rb') as f:
    image = MIMEImage(f.read())
    message.attach(image)

# Set up the SMTP server and send the email every minute
while True:
    try:
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.login(sender_email, sender_password)
        smtp_server.sendmail(sender_email, recipient_email, message.as_string())
        smtp_server.close()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    time.sleep(60)  # wait for 1 minute before sending the next email
