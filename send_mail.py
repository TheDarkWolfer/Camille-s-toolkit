import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, recipient_email, subject, message):
    try:
        # Create the email content
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Connect to the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print('Email sent successfully!')
    except Exception as e:
        print('An error occurred:', str(e))
    finally:
        # Disconnect from the server
        server.quit()

# Input email details
sender_email = 'mykelitorrice@gmail.com'
sender_password = '&TSGA2x4=yck]_P'
recipient_email = 'shadowlou@proton.me'
subject = input('TEST')
message = input('TEST')

# Call the function to send the email
send_email(sender_email, sender_password, recipient_email, subject, message)
