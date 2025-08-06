from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time


service = Service(
    r"C:\Users\jozic\PycharmProjects\Selenium_Learning\edgedriver_win32\msedgedriver.exe"
)
driver = webdriver.Edge(service=service)
driver.get("https://rahulshettyacademy.com/client")
#Finding  by hyperlink
# driver.find_element(By.LINK_TEXT,"Forgot password?").click()
# driver.find_element(By.CSS_SELECTOR,"input[type='email']").send_keys("demo@gmail.com")
# driver.find_element(By.XPATH,"(//input[@type='password'])[1]").send_keys("Mile123")
# driver.find_element(By.XPATH,"(//input[@type='password'])[2]").send_keys("Mile123")
# driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()

#Another way of finding element via XPATH(with parent/child)
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")
#Another way of finding element via CSS_SELECTOR(with parent/child)
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("mile123")
driver.find_element(By.XPATH,"(//input[@type='password'])[2]").send_keys("mile123")
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()











time.sleep(10)