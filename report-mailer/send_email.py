import resend
from config import RESEND_API_KEY, SENDER_EMAIL, RECEIVER_EMAIL

def send_email_report(html_content):
    try:
        resend.api_key = RESEND_API_KEY
        for receiver in RECEIVER_EMAIL:
            r = resend.Emails.send({
                "from": SENDER_EMAIL,
                "to": receiver,
                "subject": "Daily Report",
                "html": html_content
            })
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
