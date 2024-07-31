import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    # переходим на страницу нашего профиля
    button_profile = driver.find_element(By.CSS_SELECTOR, '.user-login.j-profile-links-loggedin')
    button_profile.click()

    lastname = driver.find_element(By.XPATH, '//input[@name="lastName" and @placeholder="Фамилия"]')
    firstname = driver.find_element(By.XPATH, '//input[@name="firstName"]')
    email = driver.find_element(By.XPATH, '//input[@name="mail"]')
    button_save = driver.find_element(By.XPATH, '//button[@type="submit" and @class="btn-primary"]')

    # прокручиваем до элемента
    driver.execute_script("arguments[0].scrollIntoView(true);", lastname)  
    # ожидаем, пока элемент не станет кликабельным
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(lastname))  
    # нажимаем на label, представляющий checkbox
    driver.execute_script("arguments[0].click();", lastname)  

    # передаем измененные данные профиля
    lastname.send_keys('Иванова')
    firstname.send_keys('Иванка')
    email.send_keys('ivanka@gmail.com')

    # сохраняем
    button_save.click()

except Exception as e:
    raise

finally:
    driver.quit()
