from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    element = browser.find_element(By.CSS_SELECTOR, 'div.first_block div.form-group.first_class input.form-control.first')
    element.send_keys("Ivan")
    time.sleep(5)
    element = browser.find_element(By.CSS_SELECTOR, 'div.first_block div.form-group.second_class input.form-control.second')
    element.send_keys("Petrov")
    time.sleep(5)
    element = browser.find_element(By.CSS_SELECTOR, 'div.first_block div.form-group.third_class input.form-control.third')
    element.send_keys("IvanPetrov@gmail.com")
    time.sleep(5)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()