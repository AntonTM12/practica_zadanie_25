import pytest
from selenium import webdriver as selenium_webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_have_name_age_and_gender(selenium_driver):
    ''' Тест на проверку списка питомцев:
       1. Проверяем, что оказались на странице питомцев пользователя.
       2. Поверяем что на странице со списком моих питомцев, у всех питомцев есть имя, возраст и порода.  '''

    driver = selenium_driver
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.nav-link[href='/my_pets']")))
    # Нажимаем на кнопку входа в пункт меню Мои питомцы
    driver.find_element(By.CSS_SELECTOR, "a.nav-link[href='/my_pets']").click()
    # time.sleep(3)
    # Проверяем, что оказались на странице питомцев пользователя
    assert driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//table[@class="table table-hover"]/tbody/tr')))
    pets_count = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')
    # time.sleep(3)
    # Перебираем данные из pet_data, оставляем имя, возраст, и породу остальное меняем на пустую строку
    # и разделяем по пробелу. Находим количество элементов в получившемся списке и сравниваем их
    # с ожидаемым результатом
    for i in range(len(pets_count)):
        data_pet = pets_count[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        result = len(split_data_pet)
        assert result == 3
        # print(result)
