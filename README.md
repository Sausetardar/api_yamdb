# API YaMDB

Учебный проект Я.Практикума, 10 спринт, 29 когорта.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Sausetardar/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
py -3.7 -m venv venv
```

```
venv\Scripts\activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

Профит!

## В проекте участвуют:
1. Maксим Усенко (Team Lead)
2. Алексей Кузьмин (Программист)
3. Игорь Бутаков (Программист)