# Kolhoz Telethon Bot on Heroku

## Как развернуть

1. Создай Heroku-аккаунт: https://signup.heroku.com  
2. Установи Heroku CLI: https://devcenter.heroku.com/articles/heroku-cli

## Установка

```bash
git clone https://github.com/yourname/kolhoz-telethon-bot.git
cd kolhoz-telethon-bot
heroku create kolhoz-filter-123
git push heroku main
```

## Установи переменные окружения

```bash
heroku config:set API_ID=26060567
heroku config:set API_HASH=9e88a5724bee290de2881c12adddfa5b
```

## Запуск

Heroku сам запустит `worker: python bot.py`
