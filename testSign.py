import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# инициализируем браузер
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

# устанавливаем размер окна браузера
driver.set_window_size(1920, 1080)

url = 'https://www.rzd.ru'

try:
    # передаем в драйвер нужный нам url сайта
    driver.get(url)
    time.sleep(2)

    # выполняем поиск и объявление нужных нам элементов
    button_login = driver.find_element(By.CSS_SELECTOR, '.j-auth-open.username')
    login = driver.find_element(By.XPATH, '//input[@name="j_username"]')
    password = driver.find_element(By.XPATH, '//input[@name="j_password" and @type="password"]')
    button_sign = driver.find_element(By.XPATH, '//button[@type="submit"]')

    # открываем форму авторизации
    button_login.click()

    # передаем данные для авторизации
    login.send_keys('test')
    password.send_keys('test')

    # входим в аккаунт
    button_sign.click()

except Exception as e:
    raise

# закрываем браузер
finally:
    driver.quit()
