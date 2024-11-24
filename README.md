# backend

---
## Переменные окружения (.env файл):
```env
# django
SECRET_KEY=<django key>
DEBUG=<True or False>
ALLOWED_HOST=<allowed hosts>

# db
DB_ENGINE=<django engine>
DB_PASSWORD=<db password>
DB_NAME=<db name>
DB_PORT=<db port>

## for local db
#DB_HOST=localhost
#DB_USER=<db user>

## for docker db
DB_HOST=db_django
CONNECT_TO_DB_LOCAL=<connect local db>
DB_USER=<db user>
```
---

## Docker

---
### Docker command:
> docker compose up --build - запуск docker контейнера

> docker compose exec -it backend-django /bin/sh - проверка файловой систему

> docker compose down - сбросить контейнер
