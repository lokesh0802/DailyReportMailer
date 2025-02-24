import os
from dotenv import load_dotenv
from pathlib import Path
from typing import Tuple, Optional

# Load environment variables from .env file
env_path = Path(__file__).parent.parent / '.env'
if not env_path.exists():
    raise FileNotFoundError(f"Environment file not found at: {env_path.absolute()}")

load_dotenv(env_path)

def mask_email(email: str) -> str:
    """Mask email address for secure logging."""
    if not email or '@' not in email:
        return ''
    username, domain = email.split('@')
    masked_username = username[:3] + '*' * (len(username) - 3)
    return f"{masked_username}@{domain}"

def get_smtp_config(email: str) -> Tuple[Optional[str], Optional[int]]:
    """Get SMTP configuration based on email domain."""
    if not email or '@' not in email:
        return None, None
    
    SMTP_SERVERS = {
        "gmail.com": ("smtp.gmail.com", 587),
        "outlook.com": ("smtp.office365.com", 587),
        "hotmail.com": ("smtp.office365.com", 587),
        "yahoo.com": ("smtp.mail.yahoo.com", 465),
        "zoho.com": ("smtp.zoho.com", 465),
        "bennett.edu.in": ("smtp.office365.com", 587),
    }
    
    domain = email.split("@")[-1].lower()
    return SMTP_SERVERS.get(domain, (None, None))

# Configuration
API_URL = "http://localhost:3000/data"
SENDER_EMAIL = os.getenv('EMAIL_USER')
SENDER_PASSWORD = os.getenv('EMAIL_APP_PASSWORD')

# Debug logging with masked email
print(f"Config initialized with email: {mask_email(SENDER_EMAIL)}")

# Get SMTP configuration
SMTP_SERVER, SMTP_PORT = get_smtp_config(SENDER_EMAIL)

if not all([SENDER_EMAIL, SENDER_PASSWORD, SMTP_SERVER, SMTP_PORT]):
    raise ValueError("""
    Missing or invalid configuration. Please ensure:
    1. .env file exists in project root
    2. EMAIL_USER and EMAIL_APP_PASSWORD are set
    3. Email domain is supported
    
    Supported email providers:
    - Gmail (@gmail.com)
    - Outlook/Hotmail (@outlook.com, @hotmail.com)
    - Yahoo (@yahoo.com)
    - Zoho (@zoho.com)
    - Bennett University (@bennett.edu.in)
    
    For Gmail setup:
    1. Enable 2-Step Verification in Google Account
    2. Generate App Password: Security → App Passwords
    3. Use the 16-character password in .env file
    """)

print(f"SMTP Configuration: {SMTP_SERVER}:{SMTP_PORT}")