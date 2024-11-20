# Необходимо реализовать скрипт, который будет получать с русскоязычной википедии список всех животных 
# (https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту) и записывать в файл в формате beasts.csv количество животных на каждую букву алфавита. 
# Содержимое результирующего файла:
# А,642
# Б,412
# В,....
# Примечание: анализ текста производить не нужно, считается любая запись из категории (в ней может быть не только название, но и, например, род)

import csv
import requests

from bs4 import BeautifulSoup

# Сюда будем добавлять буквы и их количество
result = {}

r = requests.get("https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту").text

while bool(r) == True:

    soup = BeautifulSoup(r, "lxml")

    # В блоке где список считам количество букв алфавита на которые начинаются названия животных
    block = soup.find("div", class_="mw-category mw-category-columns")
    letters_count = len(block.find_all("h3"))

    # Проходимся по всем буквам
    for _ in range(letters_count):

        # в блоке с текущей буквой
        block = block.find_next("div", class_='mw-category-group')
        letter = block.find("h3").text

        # находим все элементы списка
        list_items = block.find_all("li")
        
        if not letter in result.keys():
            result[letter] = 0
        
        # добавляем количество элементов списка в словарь, где ключ - текущая буква
        result[letter] += len(list_items)

    # Для выхода из цикла
    r = False

    links = soup.find("div", id="mw-pages").find_all('a')

    # Если есть ссылка на следующую страницу - переходим на нее и повторяем поиск
    for link in links:
        if link.text == "Следующая страница":
            r = requests.get('https://ru.wikipedia.org/' + link.get('href')).text
            break

    # Если не будет ссылки на следующую страницу - выходим из цикла
    if r == False:
        break

# Записываем результат в csv файл
with open("beasts.csv", "w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    for key,value in result.items():
        writer.writerow([key, value])