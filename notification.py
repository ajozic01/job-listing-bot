import smtplib
from email.message import EmailMessage
from config import email_config, excel_file


def send_email_notification(new_jobs):
    """
    Sends an email notification with new jobs and attaches the Excel file
    """
    if not new_jobs:
        return False

    msg = EmailMessage()
    msg["Subject"] = "New Jobs"
    msg["From"] = email_config["sender"]
    msg["To"] = email_config["receiver"]

    # Compose email body
    email_body = "New jobs have been added to RemoteOK: \n\n"
    for job in new_jobs:
        email_body += f"{job['company']}\n"
        email_body += f"{job['title']}\n"
        email_body += f"{job['url']}\n\n"
    msg.set_content(email_body)

    # Attach Excel file
    try:
        with open(excel_file, "rb") as f:
            file_data = f.read()
            msg.add_attachment(
                file_data,
                maintype="application",
                subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                filename=excel_file
            )
    except FileNotFoundError:
        print("Warning: Excel file not found. Email sent without attachment.")

    # Send the email
    try:
        with smtplib.SMTP(email_config["smtp_server"], email_config["smtp_port"]) as server:
            server.starttls()
            server.login(email_config["sender"], email_config["password"])
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
