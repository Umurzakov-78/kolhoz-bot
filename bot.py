from telethon import TelegramClient, events
from config import API_ID, API_HASH, KEYWORDS
import json
import os

client = TelegramClient('session', API_ID, API_HASH)

# Загружаем user_id (если есть)
try:
    with open("user.json", "r") as f:
        user_data = json.load(f)
        USER_ID = user_data.get("user_id")
except FileNotFoundError:
    USER_ID = None

@client.on(events.NewMessage(chats="uy_oldi_sotti_osh"))
async def handler(event):
    global USER_ID
    text = event.message.message.lower()
    if any(word in text for word in KEYWORDS):
        if USER_ID:
            await client.send_message(USER_ID, f"Обнаружено сообщение:\n\n{text}")
        else:
            print("Нет user_id — пользователь еще не писал.")

@client.on(events.NewMessage())
async def save_user(event):
    global USER_ID
    if USER_ID is None:
        USER_ID = event.sender_id
        with open("user.json", "w") as f:
            json.dump({"user_id": USER_ID}, f)
        await event.respond("Вы зарегистрированы. Теперь вы будете получать сообщения.")

print("Бот запущен.")
client.start()
client.run_until_disconnected()
