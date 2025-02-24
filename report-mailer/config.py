import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path(__file__).parent.parent / '.env'
print(f"Looking for .env file at: {env_path.absolute()}")
load_dotenv(env_path)

print(f"Loaded GMAIL_USER: {os.getenv('GMAIL_USER')}")
print(f"GMAIL_APP_PASSWORD loaded: {'Yes' if os.getenv('GMAIL_APP_PASSWORD') else 'No'}")

API_URL = os.getenv('API_URL')  


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

SENDER_EMAIL = os.getenv('GMAIL_USER')
SENDER_PASSWORD = os.getenv('GMAIL_APP_PASSWORD')

if not SENDER_EMAIL or not SENDER_PASSWORD:
    raise ValueError("""
    Please create a .env file in the project root with the following variables:
    
    GMAIL_USER=your.email@gmail.com
    GMAIL_APP_PASSWORD=your16charpassword
    
    To get an App Password:
    1. Go to your Google Account settings
    2. Enable 2-Step Verification if not already enabled
    3. Go to Security → App Passwords
    4. Select 'Mail' and generate a new app password
    5. Copy the 16-character password without spaces
    """)
