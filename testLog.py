import time
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

url = 'https://www.rzd.ru'

try:
    driver.get(url)
    time.sleep(2)

    email = driver.find_element(By.NAME, 'E-MAIL')
    login = driver.find_element(By.XPATH, '//input[@name="NAME" and @type="number"]')
    password = driver.find_element(By.XPATH, '//input[@name="userpassword" and @type="password"]')
    password_confirm = driver.find_element(By.XPATH, '//input[@name="userpassword_CONFIRM" and @type="password"]')
    firstname = driver.find_element(By.NAME, 'FIRST_NAME')
    lastname = driver.find_element(By.NAME, 'LAST_NAME')
    check = driver.find_element(By.CSS_SELECTOR, '.check__label.static-content')
    secure_code = driver.find_element(By.NAME, '_CAPTCHA_VALUE')
    button_login = driver.find_element(By.CSS_SELECTOR, '.j-auth-open.username')
    button_register = driver.find_element(By.XPATH, '//button[@data-id="reg"]')
    button_registration = driver.find_element(By.CSS_SELECTOR, '.btn-primary.login-btn')

    button_login.click()
    button_register.click()

    email.send_keys('testEmail@example.com')
    login.send_keys('testLogin')
    password.send_keys('testPassword23')
    password_confirm.send_keys('testPassword23')
    firstname.send_keys('testFirstname')
    lastname.send_keys('testLastname')

    driver.execute_script("arguments[0].scrollIntoView(true);", check)  # прокручиваем до элемента
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(check))  # ожидаем, пока элемент не станет кликабельным
    driver.execute_script("arguments[0].click();", check)  # нажимаем на label, представляющий checkbox

    driver.execute_script("arguments[0].scrollIntoView(true);", secure_code)
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(secure_code))
    except TimeoutException:
        raise
    driver.execute_script("arguments[0].click();", secure_code)
    secure_code.click()  # ожидание, что капча будет введена вручную

    driver.execute_script("arguments[0].scrollIntoView(true);", button_register)
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(button_register))
    except TimeoutException:
        raise
    driver.execute_script("arguments[0].click();", button_register)
    button_register.click()

    time.sleep(2)

except Exception as e:
    raise

finally:
    driver.quit()
