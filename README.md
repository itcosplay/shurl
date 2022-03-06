# shurl
SHURL - сервис сокращения ссылок!  
Работа сервиса демонстрируется на примере домена pythonanywhere по [ссылке](http://azuredream.pythonanywhere.com/)

# API
- Сократить ссылку:
```python
#request POST
url = 'http://azuredream.pythonanywhere.com/create'
data = {
  'url': 'http://your_very-looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong-link.com'
}
response = requests.post(url, data=data)
response.raise_for_status()

#response json
{"short_url": "http://azuredream.pythonanywhere.com/uHgch"}
```

- Создать пользовательскую ссылку:
```python
#request POST
url = 'http://azuredream.pythonanywhere.com/create_coustom'
data = {
  'url': 'http://your_link.com',
  'coustom_url': 'my-link'
}
response = requests.post(url, data=data)
response.raise_for_status()

#response json
{"short_url": "http://azuredream.pythonanywhere.com/my-link"}
```
На фронтенд части пока реализовано создание только короткой ссылки.

## Как установить
* Клонируем репозиторий
* Переменных окружение для локального развертывания не требуется
* Создаем виртуальное окружение
* Устанавливаем зависимости
```
pip install -r requirements.txt
```

## Настройка
* Выполняем миграции
```
python manage.py migrate
```
* Содаем суперпользователя
```
python manage.py createsuperuser
```

## Цели проекта
Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
