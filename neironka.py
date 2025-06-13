import telebot
import requests


TOKEN = '__'
bot = telebot.TeleBot(TOKEN)

AUTHORIZED_USERS = [1398771724]

def is_authorized(user_id):
    return user_id in AUTHORIZED_USERS

def poisk(mass):
    art = str(mass)
    base_url = f"https://alm-basket-cdn-02.geobasket.ru/vol{art[0:4]}/part{art[0:6]}/{art}"
    info_url = f"{base_url}/info/ru/card.json"

    price_url = f"{base_url}/info/price-history.json"
    response_2 = requests.get(price_url) 
    try:
        response = requests.get(info_url)
        if response.status_code and response_2.status_code == 200:
            return response.json(),response_2.json()
        else:
            return f"Ошибка: {response.status_code}",None
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
        data  = poisk(message.text)[1]


        prices = []
        for item in data:
            try:
                rub_price = item["price"]["RUB"] // 100 
                exchange_rate = 6.4
                tg_price = rub_price* exchange_rate
                prices.append(round(tg_price))
            except (KeyError, TypeError):
                continue

        if prices:
            current_price = prices[-1]
            avg_price = sum(prices) / len(prices)
            level=''
            if current_price < avg_price:
                level = "Цена ниже средней"
            elif current_price > avg_price:
                level = "Цена выше средней"
            else:
                level = "Цена равна средней"
            data_1  = poisk(message.text)[0]
            
                
            name = data_1["imt_name"]
            brand = data_1["selling"]["brand_name"]
            price = data_1["subj_name"]
            desc = data_1["description"]
                
            msg = f"Название: {name}\nБренд: {brand}\nЦена: {current_price}\nОписание: {desc}"
            bot.send_message(message.chat.id, msg)
            bot.send_message(message.chat.id, (
                    f" Средняя цена: {round(avg_price)}₸\n"
                    f" Текущая цена: {current_price}₸"
                    f"\n Уровень цены: {level}"
                ))
            
    else:
        bot.send_message(message.chat.id, 'Нет доступа')

bot.polling(True)
