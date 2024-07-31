import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

url = 'https://www.rzd.ru'

try:
    driver.get(url)
    time.sleep(2)

    button_login = driver.find_element(By.CSS_SELECTOR, '.j-auth-open.username')
    login = driver.find_element(By.XPATH, '//input[@name="j_username"]')
    password = driver.find_element(By.XPATH, '//input[@name="j_password" and @type="password"]')
    button_sign = driver.find_element(By.XPATH, '//button[@type="submit"]')

    button_login.click()

    login.send_keys('lagarce')
    password.send_keys('Lagarce3467')

    button_sign.click()

    time.sleep(2)

except Exception as e:
    raise

finally:
    driver.quit()