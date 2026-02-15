from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")
search_box=driver.find_element(By.NAME,'q')
search_box.send_keys("selenium python")
print(driver.title)
time.sleep(10)
driver.quit()