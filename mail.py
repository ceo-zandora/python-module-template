import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email_with_apk(sender_email, sender_password, receiver_email, subject, message, apk_path):
    # SMTP server configuration
    smtp_server = 'smtp.example.com'
    smtp_port = 587

    # Create a multipart message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Add the message body
    msg.attach(MIMEText(message, 'plain'))

    # Open the APK file
    with open(apk_path, 'rb') as apk_file:
        # Create the application/octet-stream attachment
        apk_part = MIMEApplication(apk_file.read(), Name='app.apk')
    
    # Add the attachment to the message
    apk_part['Content-Disposition'] = 'attachment; filename="app.apk"'
    msg.attach(apk_part)

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)

# Example usage
sender_email = 'your_email@example.com'
sender_password = 'your_password'
receiver_email = 'recipient@example.com'
subject = 'Email with APK attachment'
message = 'Hello, please find the APK file attached.'
apk_path = '/path/to/your/app.apk'

send_email_with_apk(sender_email, sender_password, receiver_email, subject, message, apk_path)
