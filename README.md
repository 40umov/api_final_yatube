### Проект API для социальной сети Yatube

Yatube это социальная сеть где можно делится постами, вступать в группы и подписываться на авторов.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git@github.com:40umov/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3.9 -m venv venv
```

```
source venv/bin/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Перейти в каталог api_final_yatube/yatube_api и выполнить миграции:

```
cd yatube_api
```

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
Все endpoints запросов к API можно получить используя команду:

```
python manage.py show_urls
````

### Примеры запросов к API

Получение публикаций:
```
http://127.0.0.1:8000/api/v1/posts/
```
Получение списка доступных сообществ:
```
http://127.0.0.1:8000/api/v1/groups/
```
Получение комментария к публикации по id:

```
http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
```