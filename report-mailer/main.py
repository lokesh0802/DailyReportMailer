from fetch_data import fetch_report_data
from generate_report import generate_html_report
from send_email import send_email_report
from datetime import datetime

def main():
    print(f"Starting daily report generation at {datetime.now()}")
    email_grouped_data = fetch_report_data()
    
    if not email_grouped_data:
        print("No data to process")
        return
        
    print(f"Found data for {len(email_grouped_data)} unique email addresses")

    email_reports = {}
    for email, client_data in email_grouped_data.items():
        try:
            html_content = generate_html_report(client_data)
            if html_content:
                email_reports[email] = html_content
                print(f"Generated report for {email} ({len(client_data)} records)")
            else:
                print(f"No report generated for {email} - invalid data format")
        except Exception as e:
            print(f"Error generating report for {email}: {str(e)}")

    if email_reports:
        print(f"Sending {len(email_reports)} reports...")
        send_email_report(email_reports)
    else:
        print("No reports generated - no valid client data found")
    
    print(f"Report generation completed at {datetime.now()}")

if __name__ == "__main__":
    main()
