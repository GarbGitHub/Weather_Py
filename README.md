# Weather - Погода в городах мира
Это погодное приложение, которое автоматически определяет местную погоду на основе внешнего IP-адреса пользователя. 
По запросу пользователя, приложение предоставляет погодные данные в разных регионах мира.
 
Данные представляются популярным погодного сервиса openweathermap.org.

# Настройки
<ul>
    <li>Установить зависимости pip install -r requirements.txt</li>
    <li>Переименуйте файл !_key_owm в key_owm</li>
    <li>В файле key_owm вставьте свой ключ полученный на openweathermap.org. Для регистрации нового аккаунта воспользуйтесь ссылкой https://home.openweathermap.org/users/sign_up</li>
    <li>Файл setup.py поможет правильно скомпилировать запускаемые программу файлы в cx_Freeze:
        <ul>
        <li>pip install cx_freeze</li>
        <li>python setup.py build</li>
        </ul>
    </li>
</ul>
<p>В результате успешной компиляции будет создана папка <b>build</b> с файлами внутри.</p>
<p>Во время работы программы создается и перезаписывается файл <b>settings.txt</b> отвечающий за текущий город. Такое поведение 
может вызвать ложное срабатывание некоторых антивирусных программ. Для нормальной работы приложения, в случае необходимости
 предоставьте необходимое исключение в вашем антивирусе.</p>

# Функциональность и логика
<s>При запуске приложение изначально проверяет файл settings.txt на наличие города по умолчанию. Если такая запись есть, 
выводится погодная информация данному городу. Если записи нет, или файл еще не создан, приложение определяет текущий город и записывает его в settings.txt.</s><br>
Начиная с версии 0.0.2 хранение данных производится в базе данных SQLite. При первом запуске текущая локация или город узнается у Яндекса и сохраняется в БД. 
Это, позволяет исключить регулярные автоматические запросы приложения для определения местоположения. В настройках программы пользователь может в ручную задать город по умолчанию.

<h3>Пример вывода информации:</h3>
Москва,
понедельник пасмурно,
погодная иконка,
3°, влажность 95%, ветер 5 м./c.
