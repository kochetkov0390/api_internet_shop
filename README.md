# api_internet_shop
Проект сервиса API интернет магазина для стажировки в IT Code.

## Как запустить проект:

__Клонировать репозиторий и перейти в него в командной строке:__

```
git clone https://github.com/kochetkov0390/api_internet_shop
```

```
cd api_internet_shop
```

__Cоздать и активировать виртуальное окружение:__

```
python -m venv venv 
```

```
source env/bin/activate
```

```
python -m pip install --upgrade pip
```

__Установить зависимости из файла requirements.txt:__

```
pip install -r requirements.txt
```

__Выполнить миграции:__

```
python manage.py migrate
```
__Создать суперюзера:__
```
python manage.py createsuperuser
```

__Запустить проект:__

```
python manage.py runserver
```
Проект доступен по адресу http://127.0.0.1:8000/admin/

__Примеры роутов:__

```
http://127.0.0.1:8000/api/categories/
http://127.0.0.1:8000/api/smartphones/
http://127.0.0.1:8000/api/notebooks/<str:pk>/

```
