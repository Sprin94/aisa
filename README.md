# aisa
# Стек

Python, Django, DRF.


## Приложение
Сервис для сокращения ссылок

### API

Реализованы эндпоинты:

### Управление станциями
* GET: /
    Возвращает страницу с полями для получения короткой ссылки.
* POST: api/short_url/
    Создание сокращенного URL
    * Схема запроса:
        * url- URL адрес, который будет сокращен
    * Схема ответа:
        * url- URL адрес, который был сокращен
        * short_url - сокращенный URL

# Использование
1. Склонируйте данный репозиторий на свою локальную машину
2. Убедитесь, что у вас установлен пакет [Poetry](https://python-poetry.org/docs/)
3. Установите зависимости командой:
```sh
poetry install 
```
4. Примените миграции:
```sh
python manage.py migrate
```

5. Для запуска сервера используйте команду:
```sh
python manage.py runserver
```
