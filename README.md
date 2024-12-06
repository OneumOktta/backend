# backend

---
## Переменные окружения (.env файл):
```env
# django
SECRET_KEY=<django key>
DEBUG=<True or False>
ALLOWED_HOST=<allowed hosts>

# email
EMAIL_BACKEND=<django path>
EMAIL_HOST=<host mail>
EMAIL_PORT=<port mail>
EMAIL_USE_SSL=<ssl mail>
EMAIL_HOST_USER=<your mail>
EMAIL_HOST_PASSWORD=<smtp password>

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
---
## EMAIL SMTP

---

***[Ссылка на создание почты](https://help.mail.ru/mail/mailer/2fa/)***

Пароль необходимо скопировать и вставить в файл .env в переменную EMAIL_HOST_PASSWORD

***[Ссылка на получение дополнительной информации](https://help.mail.ru/mail/mailer/popsmtp/)***
