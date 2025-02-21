import requests
from config import API_URL

def fetch_report_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  
        return response.json() 
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
