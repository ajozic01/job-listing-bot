# config.py
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# RemoteOK URL
remote_ok_url = "https://remoteok.com/remote-dev-jobs"

# Excel file
excel_file = "remote_jobs.xlsx"

# Email config from environment
email_config = {
    "sender": os.getenv("EMAIL_SENDER"),
    "receiver": os.getenv("EMAIL_RECEIVER"),
    "password": os.getenv("EMAIL_PASSWORD"),
    "subject": os.getenv("EMAIL_SUBJECT"),
    "smtp_server": os.getenv("SMTP_SERVER"),
    "smtp_port": int(os.getenv("SMTP_PORT")),
}

# PostgreSQL config from environment
db_config = {
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "port": int(os.getenv("DB_PORT")),
}
