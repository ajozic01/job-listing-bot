# 🛎️ Job Notifier Bot

An automated bot that scrapes remote job listings from [RemoteOK](https://remoteok.com/), stores them in Excel and a PostgreSQL database, and sends email notifications when new jobs are found.

## 🚀 Features

- ✅ Scrapes fresh job listings using **Selenium**
- ✅ Saves results to an **Excel file**, avoiding duplicates
- ✅ Inserts new jobs into a **PostgreSQL database**
- ✅ Sends **email notifications** for new listings
- ✅ Runs automatically every hour

## 📂 Project Structure

Job_Notifier_Bot/
│
├── config.py # Configuration (URLs, email, DB credentials)
├── database.py # PostgreSQL connection and insert logic
├── scraper.py # Selenium scraping logic
├── storing.py # Excel storage using pandas
├── notification.py # Email notification system
├── main.py # Main script (runs every hour)
├── requirements.txt # Dependencies
└── README.md # Project documentation


## 🧰 Tech Stack

- **Python 3**
- **Selenium**
- **Pandas**
- **PostgreSQL**
- **smtplib** (email)
- **OpenPyXL** (Excel writing)

