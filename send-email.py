import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Email configuration
sender_email = 'your_email@gmail.com'
receiver_email = 'recipient_email@example.com'
subject = 'Hello from Python!'
message = 'This is a test email sent from a Python program.'

# SMTP server configuration (for Gmail, change the server and port accordingly)
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'your_email@gmail.com'
smtp_password = 'your_email_password'

# Create the email message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

# Create and attach a file (optional)
# with open('attachment.txt', 'rb') as file:
#     attach = MIMEApplication(file.read(),_subtype="txt")
#     attach.add_header('Content-Disposition', 'attachment', filename='attachment.txt')
#     msg.attach(attach)

# Connect to the SMTP server and send the email
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Use TLS for encryption
    server.login(smtp_username, smtp_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    server.quit()
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {str(e)}")
