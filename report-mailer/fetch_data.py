import requests
from config import API_URL

def fetch_report_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        data = response.json()
        
        if not data or not isinstance(data, list) or len(data) == 0:
            print("No data received from API")
            return None

        email_data = {}
        records = data[0].get('get_sales_breakup_by_email_new', [])
        
        for record in records:
            email = record.get('email')
            if email:
                if email not in email_data:
                    email_data[email] = []
                email_data[email].append(record)
        
        return email_data
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    except (KeyError, IndexError, TypeError) as e:
        print(f"Error processing data: {e}")
        return None
