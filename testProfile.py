import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
# chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

driver.set_window_size(1920, 1080)

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

    button_profile = driver.find_element(By.CSS_SELECTOR, '.user-login.j-profile-links-loggedin')
    button_profile.click()

    lastname = driver.find_element(By.XPATH, '//input[@name="lastName" and @placeholder="Фамилия"]')
    firstname = driver.find_element(By.XPATH, '//input[@name="firstName"]')
    email = driver.find_element(By.XPATH, '//input[@name="mail"]')
    button_save = driver.find_element(By.XPATH, '//button[@type="submit" and @class="btn-primary"]')

    driver.execute_script("arguments[0].scrollIntoView(true);", lastname)  # прокручиваем до элемента
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(lastname))  # ожидаем, пока элемент не станет кликабельным
    driver.execute_script("arguments[0].click();", lastname)  # нажимаем на label, представляющий checkbox

    lastname.send_keys('Иванова')
    firstname.send_keys('Иванка')
    email.send_keys('ivanka@gmail.com')

    button_save.click()
    time.sleep(2)

except Exception as e:
    raise

finally:
    driver.quit()