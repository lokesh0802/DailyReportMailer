from fetch_data import fetch_report_data
from generate_report import generate_html_report
from send_email import send_email_report

def main():
    data = fetch_report_data()
    if data:
        html_content = generate_html_report(data)
        send_email_report(html_content)

if __name__ == "__main__":
    main()
