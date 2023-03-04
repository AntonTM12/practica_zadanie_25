import pytest
from selenium import webdriver as selenium_webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_diferent_name_pets(selenium_driver):
    ''' Тест на проверку списка питомцев:
       1. Проверяем, что оказались на странице питомцев пользователя.
       2. У всех питомцев разные имена.  '''


    driver = selenium_driver
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.nav-link[href='/my_pets']")))
    # Нажимаем на кнопку входа в пункт меню Мои питомцы
    driver.find_element(By.CSS_SELECTOR, "a.nav-link[href='/my_pets']").click()
    # time.sleep(3)
    # Проверяем, что оказались на странице питомцев пользователя
    assert driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'

    # 1. Проверяем, что присутствуют все питомцы, для этого:
    # находим кол-во питомцев по статистике пользователя
    pets_number = driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(': ')[1]
    # pets_count = 100
    names = driver.find_elements(By.XPATH, '//*[@id="all_my_pets"]/table/tbody/tr/td[1]')
    time.sleep(3)
    # проверяем, что их число соответствует кол-ву имен питомцев
    assert int(pets_number) == len(names)
    # Перебираем данные и добавляем их в список

    pets_name = []
    for i in names:
        one_name = i.text
        pets_name.append(one_name)
        # print(pets_name)

    # Перебираем имена и если имя повторяется то прибавляем к счетчику count единицу.
    # Проверяем, если count == 0 то повторяющихся имен нет.
    count = 0


    try:
        for i in range(len(pets_name)):
            if pets_name.count(pets_name[i]) > 1:
                count += 1
        assert count == 0
        print(count)
        print(pets_name)
    except AssertionError:
        print(f'{count} питомца имееет  одинаковое имя')
