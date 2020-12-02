import bs4 as bs4
import requests
import sqlite3


def yandex_internet():
    """Определяется текущий город с помощью Яндекс Интернетометра https://yandex.ru/internet/"""

    s_host = requests.get('https://yandex.ru/internet/')
    ds = bs4.BeautifulSoup(s_host.text, "html.parser")
    city = ds.select(" .location-renderer .location-renderer__value")[0].getText()
    return city


def sett_city():
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    # Если таблицы нет - создаем ее
    sql.execute("""CREATE TABLE IF NOT EXISTS cities (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    `city` TEXT)""")
    db.commit()

    # Если таблица пустая - делаем первую запись, город узнаем у Яндекса
    sql.execute('SELECT city FROM cities')
    if sql.fetchone() is None:
        city = yandex_internet()
        sql.execute(f"INSERT INTO cities (city) VALUES('{city}')")
        db.commit()
        db.close()
        return city

    # Если в таблице есть город, работаем с ним
    else:
        sql.execute(f"SELECT city FROM cities WHERE id = {1}")
        city = sql.fetchone()[0]
        db.close()
        return city


def ed_city(new_city):
    """Пользователь сохраняет в БД свой город"""

    db = sqlite3.connect('server.db')
    sql = db.cursor()
    if new_city == '':  # Если пользователь не ввел город
        new_city = yandex_internet()  # Берем город у Яндекса
    sql.execute(f"UPDATE cities SET city = '{new_city}' WHERE id = {1}")
    db.commit()
    db.close()
