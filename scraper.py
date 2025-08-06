import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from config import remote_ok_url


def scrape_remote_jobs():
    """
    Scrape remote jobs from RemoteOK page

    """
    options = Options()
    options.add_argument("--headless")  # Run without opening browser
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")


    service = Service(
        r"C:\Users\jozic\PycharmProjects\Job_Notifier_Bot\edgedriver_win32\msedgedriver.exe"
    )
    driver = webdriver.Edge(service=service, options=options)
    jobs = []
    try:
        driver.get(remote_ok_url)
        time.sleep(3)
        job_rows = driver.find_elements(By.CSS_SELECTOR, "tr.job")
        for job_row in job_rows:
            try:
                title_elem = job_row.find_element(By.CSS_SELECTOR, "h2")
                company_elem = job_row.find_element(By.CSS_SELECTOR, "h3")
                url_elem = job_row.find_element(By.CSS_SELECTOR, "a")
                title = title_elem.text if title_elem else "No Title"
                company = company_elem.text if company_elem else "No Company"
                url = url_elem.get_attribute("href") if url_elem else "No URL"
                if url:
                    jobs.append({"title": title, "company": company, "url": url})

            except Exception as e:
                print(f"Error parsing jobs : {e}")
                continue

        return jobs
    except Exception as e:
        print(f"Error fetching jobs: {e}")
        return []
    finally:
        driver.quit()
