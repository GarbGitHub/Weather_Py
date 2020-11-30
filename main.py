import webbrowser
import bs4
import pyowm
import requests
from pyowm.utils.config import get_default_config
from datetime import date
from tkinter import *
from settings_city import sett_city, ed_city
from key_owm import key_owm

version = '0.0.1'
city = sett_city()

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = pyowm.OWM(key_owm)  # You need to rename !_key_owm.py to key_owm.py
day = date.today().weekday()
week = {'0': 'понедельник', '1': 'вторник', '2': 'среда', '3': 'четверг', '4': 'пятница', '5': 'суббота',
        '6': 'воскресение'}

day_result = week[f'{str(day)}']


def win_city():
    def change_text_btn(event):
        """Замена текста кнопки с заменой цвета"""

        if city_page_button['fg'] == 'red':
            city_page_button['fg'] = 'blue'
        else:
            city_page_button['fg'] = 'red'
        city_page_button['text'] = "Сохранено!"
        page_city.after(800, page_city.destroy)

    page_city = Toplevel()
    page_city.resizable(width=False, height=False)
    page_city.geometry('250x200-40+40')
    page_city.title('Город')
    page_city['bg'] = '#ffffff'
    page_city.iconphoto(False, PhotoImage(file='app_icon.png'))

    # Поле ввода
    city_page_field = Entry(
        page_city,
        font='Arial 11',
        relief='solid',
        justify='center',
        bg="white",
        highlightcolor='#ffffff',
        highlightbackground='#dadada',
        highlightthickness=0,
    )
    city_page_field.insert(0, city.title())

    # Кнопка Сохранить
    city_page_button = Button(
        page_city,
        command=lambda: ed_city(city_page_field.get()),
        text='Сохранить',
        width=12,
        font='Arial 8',
        relief=FLAT,
        overrelief=GROOVE,
        height=0,
        pady=2
    )
    city_page_button.bind('<Button-1>', change_text_btn)
    city_page_button.bind('<Return>', change_text_btn)

    city_page_field.pack(side=TOP, pady=10)
    city_page_button.pack(side=TOP, pady=4)


def win_app_version():
    global version
    page_version = Toplevel()
    page_version.resizable(width=False, height=False)
    page_version.geometry('250x200-40+40')
    page_version.title('О программе')
    page_version['bg'] = '#ffffff'
    page_version.iconphoto(False, PhotoImage(file='app_icon.png'))

    # Версия
    txt_version = Label(
        page_version,
        text=f'Текущая версия программы: \n{version}',
        bg='#ffffff',
        font='Arial 10',
    )
    txt_version.pack(side=TOP, pady=4)

    def callback(a: str = ''):
        webbrowser.open_new(f"https://www.garb.ru/download/weather_app/weather_{a}.zip")
        webbrowser.open_new(f"https://www.garb.ru/mob-app/weather-cities-world/")

    def go_def_version():
        """Проверка обновлений приложения на сайте разработчика"""

        btn_up_version.pack_forget()
        global version
        version_app = version
        s_host = requests.get('https://www.garb.ru/mob-app/weather-cities-world/')
        ds = bs4.BeautifulSoup(s_host.text, "html.parser")
        new_version_app = ds.select(" .version_app .current_version")[0].getText()
        if version_app == new_version_app:
            result_search_version['text'] = 'Обновлений не найдено'
        else:
            result_search_version['text'] = f'Найдена новая версия \n {new_version_app}'
            link_www = Label(page_version, text="Скачать с сайта программы", fg="blue", bg="#FFFFFF", cursor="hand2")
            link_www.pack()
            link_www.bind("<Button-1>", lambda event: callback(new_version_app))

        return version_app

    btn_up_version = Button(
        page_version,
        command=lambda: go_def_version(),
        text='Проверить на обновление',
        width=24,
        font='Arial 8',
        relief=FLAT,
        overrelief=GROOVE,
        height=0,
        pady=2
    )
    btn_up_version.pack(side=TOP, pady=4)

    result_search_version = Label(
        page_version,
        text='',
        bg='#ffffff',
        font='Arial 10',
    )
    result_search_version.pack(side=TOP, pady=4)

    home_page_www = Label(page_version, text="© S.Kluikov: www.garb.ru", fg="DarkGray", bg="#FFFFFF", cursor="hand2")
    home_page_www.pack()
    home_page_www.bind("<Button-1>", callback)
    home_page_www.pack()
    home_page_www.place(relx=0.07, rely=0.87, relwidth=0.86, relheight=0.09)


# Window setting
root = Tk()
root.resizable(width=False, height=False)
root.geometry('400x400-50+50')
root.title('Погода')
root.wm_attributes('-alpha', 0.9)
root['bg'] = '#ffffff'
root.iconphoto(False, PhotoImage(file='app_icon.png'))

mainmenu = Menu(root)
root.config(menu=mainmenu)
settings_menu = Menu(mainmenu, tearoff=0)
settings_menu.add_command(label="Город по умолчанию", command=win_city)
helpmenu = Menu(mainmenu, tearoff=0)
helpmenu.add_command(label="О программе", command=win_app_version)
mainmenu.add_cascade(label="Настройки", menu=settings_menu)
mainmenu.add_cascade(label="Справка", menu=helpmenu)

frame_top = Frame(root, bg='#ffffff', bd=5)
frame_top.place(relx=0.05, rely=0.0, relwidth=0.9, relheight=0.9)
frame_bottom = Frame(root, bg='#f8ec24', bd=5)
frame_bottom.place(relx=0.07, rely=0.87, relwidth=0.86, relheight=0.09)

# City
text_search = Label(
    frame_top,
    text=f'{city.title()}',
    bg='#ffffff',
    font='Arial 22'
)

# День ннедели, краткая информация
day = Label(
    frame_top,
    text=f'{day_result}, ',
    bg='#ffffff',
    font='Arial 12',
)

# Погодная иконка
img_n = PhotoImage(file='', format='png')
img_ic = Label(frame_top, image=img_n, borderwidth=0, highlightthickness=0)
img_ic.image_ref = img_n

color_temp_plus_1 = '#ff3333'
color_temp_plus_2 = '#cc6666'
color_temp_plus_3 = '#996666'

# Температура
temp_city = Label(
    frame_top,
    text='',
    bg='#ffffff',
    fg='#666666',
    font='Arial 35'
)

# Погодная информация
info = Label(
    frame_top,
    text='Погодная информация',
    bg='#ffffff',
    font='Arial 10',
)

# Поле ввода
cityfield = Entry(
    frame_bottom,
    font='Arial 13',
    relief='solid',
    justify='center',
    bg="white",
    highlightcolor='#ffffff',
    highlightbackground='#dadada',
    highlightthickness=0,
    width=24
)

# Кнопка
enter_button = Button(
    frame_bottom,
    text='Узнать погоду',
    relief=FLAT,
    overrelief=GROOVE,
    command=lambda: push_weather(cityfield.get()),
    # height=3,
    width=12,
    font='Arial 10'
)

# Packer
text_search.pack(side=TOP)
day.pack(side=TOP)
img_ic.pack(side=TOP)
temp_city.pack(side=TOP)
info.pack(side=TOP)
cityfield.pack(side=LEFT)
enter_button.pack()


def push_weather(pull_sity):
    try:
        global img_n
        city = pull_sity
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(city)
        weather = observation.weather
        temp = weather.temperature('celsius')['temp']  # из словаря celsius берем температуру
        hum = weather.humidity  # влажность
        wd = weather.wind()['speed']  # ветер
        status = weather.detailed_status  # статус
        icon = weather.weather_icon_name

        hum_res = f'Влажность: {str(hum)}%, '
        wd_res = f'Ветер: {str(wd)} м/с\n'
        info['text'] = hum_res + wd_res
        status_res = f'{str(status)}\n'
        text_search['text'] = f'{city.title()}'
        day['text'] = f'{day_result.title()}, {status_res}'
        img_n['file'] = f'weather_icons/{icon}@2x.png'
        temp_city['text'] = f'{str(int(temp))}°C'

        if int(temp) > 14:
            temp_city['fg'] = '#FF0000'
        elif 5 < int(temp) <= 14:
            temp_city['fg'] = '#CD5C5C'
        elif 0 <= int(temp) <= 5:
            temp_city['fg'] = '#FA8072'
        elif 0 > int(temp) >= -5:
            temp_city['fg'] = '#00BFFF'
        else:
            temp_city['fg'] = '#003399'

    except pyowm.commons.exceptions.NotFoundError:
        info['text'] = 'Такой город не найден'
    except pyowm.commons.exceptions.APIRequestError:
        info['text'] = 'Задан пустой запрос'


push_weather(city)
root.mainloop()
