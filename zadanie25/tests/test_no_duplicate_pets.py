import pytest
from selenium import webdriver as selenium_webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_no_duplicate_pets(selenium_driver):
    ''' Тест на проверку списка питомцев:
       1. Проверяем, что оказались на странице питомцев пользователя.
       2. В списке нет повторяющихся питомцев.  '''

    driver = selenium_driver
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.nav-link[href='/my_pets']")))
    # Нажимаем на кнопку входа в пункт меню Мои питомцы
    driver.find_element(By.CSS_SELECTOR, "a.nav-link[href='/my_pets']").click()
    # time.sleep(3)
    # Проверяем, что оказались на странице питомцев пользователя
    assert driver.current_url == 'https://petfriends.skillfactory.ru/my_pets'

    # 1. Проверяем, что присутствуют все питомцы, для этого:
    # находим кол-во питомцев по статистике пользователя и проверяем, что их число
    # соответствует кол-ву питомцев в таблице
    pets_number = driver.find_element(By.XPATH, '//div[@class=".col-sm-4 left"]').text.split('\n')[1].split(': ')[1]
    # pets_count = 100
    pets_count = driver.find_elements(By.XPATH, '//table[@class="table table-hover"]/tbody/tr')
    time.sleep(3)
    assert int(pets_number) == len(pets_count)


    # Перебираем данные из pets_count, оставляем имя, возраст, и породу остальное меняем на пустую строку
    # и разделяем по пробелу.
    list_data = []
    for i in range(len(pets_count)):
        data_pet = pets_count[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        list_data.append(split_data_pet)
    # print(list_data)
    # print(type(list_data))
    # Склеиваем имя, возраст и породу, получившиеся склееные слова добавляем в строку
    # и между ними вставляем пробел

    line = ''
    for i in list_data:
        line += ''.join(i)
        line += ' '
    # print(line)
    # print(type(line))

    # # Получаем список из строки line
    list_line = line.split(' ')
    # print(list_line)
    # print(type(list_line))
    # Перебираем получившиеся склееные слова и если получившиеся склееные слова повторяется то прибавляем к счетчику count единицу.
    # Проверяем, если count == 0 то повторяющихся получившиеся склееные слова нет.

    count = 0

    try:
        for i in range(len(list_line)):
            if list_line.count(list_line[i]) > 1:
                count += 1
        assert count == 0
        print(count)
        # print(list_line)
    except AssertionError:
        print(f'{count} питомца дубликаты')
