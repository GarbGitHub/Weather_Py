import bs4 as bs4
import requests
import os.path


def sett_city():
    """Получаем город из файла settings.txt, если его нет - создается файл"""

    print('set_city')
    if os.path.isfile('settings.txt'):
        with open('settings.txt', 'r', encoding='utf-8') as set_file:
            city = set_file.readline()
            if city == '':
                city = yandex_internet()
                with open('settings.txt', 'w', encoding='utf-8') as set_file:
                    set_file.write(city)
            return city
    else:
        with open('settings.txt', 'w', encoding='utf-8') as set_file:
            city = yandex_internet()
            set_file.write(city)
        return city


def yandex_internet():
    """Определяется текущий город с помощью Яндекс Интернетометра https://yandex.ru/internet/"""

    s_host = requests.get('https://yandex.ru/internet/')
    ds = bs4.BeautifulSoup(s_host.text, "html.parser")
    city = ds.select(" .location-renderer .location-renderer__value")[0].getText()
    return city


def ed_city(new_city):
    """Пользователь вносит город по умолчанию в settings.txt"""

    with open('settings.txt', 'w', encoding='utf-8') as new_file:
        new_file.write(new_city)
