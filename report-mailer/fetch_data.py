import requests
from config import API_URL

def fetch_report_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raises error if the request fails
        return response.json()  # Return JSON data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
