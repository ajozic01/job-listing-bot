from scraper import scrape_remote_jobs
from storing import save_jobs_to_excel
from notification import send_email_notification
from database import insert_jobs  # ✅ Import database insert function
import time


def run_scraper():
    print("Starting RemoteOK scraper...")

    # Step 1: Scrape jobs
    jobs = scrape_remote_jobs()
    print(f"Found {len(jobs)} jobs on RemoteOK site")

    # Step 2: Save to Excel and filter new jobs
    new_jobs = save_jobs_to_excel(jobs)
    print(f"Found {len(new_jobs)} new jobs")

    # Step 3: Insert new jobs into PostgreSQL
    if new_jobs:
        inserted = insert_jobs(new_jobs)
        print(f"{inserted} new jobs inserted into database")

        # Step 4: Send notification
        send_email_notification(new_jobs)
        print("Notification sent successfully")
    else:
        print("No new jobs to notify or insert")


if __name__ == "__main__":
    while True:
        run_scraper()
        time.sleep(3600)
