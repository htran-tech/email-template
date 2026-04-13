#!/usr/bin/env python3
"""
Quick script to send test emails with HTML content
Usage: python send-test-email.py
"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_test_email():
    # Configuration
    sender_email = "your-email@gmail.com"  # Change this
    receiver_email = "test-recipient@gmail.com"  # Change this
    password = "your-app-password"  # Use Gmail App Password, not regular password

    # Read HTML file
    with open('test-hero-variants.html', 'r') as file:
        html_content = file.read()

    # Create message
    message = MIMEMultipart("alternative")
    message["Subject"] = "Test: Hero Variants"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Add HTML content
    html_part = MIMEText(html_content, "html")
    message.attach(html_part)

    # Send email
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print(f"✅ Test email sent to {receiver_email}")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nNote: Use Gmail App Password, not regular password")
        print("Get one here: https://myaccount.google.com/apppasswords")

if __name__ == "__main__":
    send_test_email()
