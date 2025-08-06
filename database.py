import psycopg2
from config import  db_config

def connect():
    return psycopg2.connect(**db_config)

def insert_jobs(jobs):
    conn=connect()
    cur=conn.cursor()
    inserted=0
    for job in jobs:
        try:
            cur.execute(
                """
                INSERT INTO jobs(title,company,url)
                VALUES(%s,%s,%s)
                ON CONFLICT(url) DO NOTHING
                """,
                (job["title"],job["company"],job["url"])
            )
            inserted+=cur.rowcount
        except psycopg2.Error as e:
            print(f"Error while connecting to PostgreSQL: {e}")
            continue
    conn.commit()
    cur.close()
    conn.close()
    return inserted
