# Сервис BakeCake

Бот для автоматизации заказов тортов BakeCake.

## Как установить
Скачайте репозиторий и установите Python пакеты из `requirements.txt`:
```bash
git clone https://github.com/AlexRikka/BakeCakebot.git
cd beautycitybot
pip install -r requirements.txt
```

Чтобы запустить бота используйте следующюю команду из корня проекта:
```
python manage.py bot
```

Для взаимодействия с API сервисов необходимо получить их API токены. Создайте в папке с проектом файл `.env` и добавляйте переменные с токенами в него.
Какие переменные `.env` понадобятся:  
- TG_BOT_HTTP_KEY=<токен телеграм бота>


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
