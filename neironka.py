import telebot
import requests

TOKEN = '7955204064:AAHIPbfq8qok8w2Q7LfhgbB8pcvMhEioNWo'
bot = telebot.TeleBot(TOKEN)

AUTHORIZED_USERS = [1398771724]

def is_authorized(user_id):
    return user_id in AUTHORIZED_USERS

def poisk(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            return response.json()
        else:
            return f"Ошибка: {response.status_code}"
    except Exception as e:
        return f"Ошибка запроса: {e}"

@bot.message_handler(commands=['start'])
def start_message(message):
    if is_authorized(message.chat.id):
        bot.send_message(message.chat.id, f'Добро пожаловать! Ваш ID: {message.chat.id}')
    else:
        bot.send_message(message.chat.id, 'Нет доступа')

@bot.message_handler(content_types=['text'])
def message_reply(message):
    if is_authorized(message.chat.id):
        data  = poisk(message.text)

        name = data["imt_name"]
        brand = data["selling"]["brand_name"]
        price = data["subj_name"]
        desc = data["description"]
        msg = f"Название: {name}\nБренд: {brand}\nЦена: {price}\nОписание: {desc}"
        bot.send_message(message.chat.id, msg)
    else:
        bot.send_message(message.chat.id, 'Нет доступа')

bot.polling(True)
