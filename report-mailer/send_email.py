import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import socket
from config import SMTP_SERVER, SMTP_PORT, SENDER_EMAIL, SENDER_PASSWORD

def verify_smtp_connection():

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.quit()
        return True, "SMTP connection successful"
    except smtplib.SMTPAuthenticationError:
        return False, """
        Gmail authentication failed. Please verify:
        1. Environment variables are set correctly:
           - GMAIL_USER
           - GMAIL_APP_PASSWORD
        2. You're using an App Password, not your regular Gmail password
        3. The App Password is typed correctly (16 characters)
        4. 2-Step Verification is enabled for your Google Account
        """
    except socket.gaierror:
        return False, "Cannot connect to SMTP server. Please check your internet connection."
    except Exception as e:
        return False, f"SMTP connection error: {str(e)}"

def send_email_report(email_reports):
    
    # First verify SMTP connection
    success, message = verify_smtp_connection()
    if not success:
        print(f"SMTP Connection Error:\n{message}")
        return
        
    server = None
    try:
        # Connect to SMTP server
        print("Connecting to SMTP server...")
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        
        # Login
        print(f"Logging in as {SENDER_EMAIL}...")
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        
        success_count = 0
        failed_emails = []
        
        total_emails = len(email_reports)
        print(f"\nSending {total_emails} reports...")
        
        # Send to each recipient
        for recipient_email, html_content in email_reports.items():
            try:
                # Create message
                msg = MIMEMultipart('alternative')
                msg['Subject'] = f'Daily Sales Report - {datetime.now().strftime("%Y-%m-%d")}'
                msg['From'] = f"Daily Reports <{SENDER_EMAIL}>"
                msg['To'] = recipient_email
                
                # Attach HTML content
                html_part = MIMEText(html_content, 'html')
                msg.attach(html_part)
                
                # Send email
                server.send_message(msg)
                success_count += 1
                print(f"✓ Sent to {recipient_email}")
                
            except Exception as e:
                failed_emails.append(recipient_email)
                print(f"✗ Failed to send to {recipient_email}: {str(e)}")
        
        # Print summary
        print(f"\nEmail Sending Summary:")
        print(f"Successfully sent: {success_count}/{total_emails}")
        if failed_emails:
            print(f"Failed recipients: {', '.join(failed_emails)}")
            
    except smtplib.SMTPAuthenticationError:
        print("""
        Gmail authentication failed!
        Please check your environment variables:
        1. GMAIL_USER should be your full Gmail address
        2. GMAIL_APP_PASSWORD should be a 16-character App Password
           (Not your regular Gmail password)
        
        To generate an App Password:
        1. Go to your Google Account settings
        2. Security → 2-Step Verification → App Passwords
        3. Generate a new password for 'Mail'
        """)
    except Exception as e:
        print(f"Error in email sending process: {str(e)}")
        
    finally:
        if server:
            try:
                server.quit()
                print("SMTP connection closed")
            except:
                pass 
