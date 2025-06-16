from config import *
from core import *

import telebot



TOKEN = '__'
bot = telebot.TeleBot(TOKEN)



def is_authorized(user_id):
    return user_id in AUTHORIZED_USERS


    

@bot.message_handler(commands=['start'])
def start_message(message):
    if is_authorized(message.chat.id):
        bot.send_message(message.chat.id, f'Добро пожаловать! Ваш ID:{message.chat.id}')
    else:
        bot.send_message(message.chat.id, f'Нет доступа,Ваш ID::{message.chat.id}')


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if is_authorized(message.chat.id):
        data_ochenk = poisk(message.text)[3]
        for i in data_ochenk['data']['products']:
            ReviewRating=i['nmReviewRating']

            Feedbacks=i['nmFeedbacks']
    
            
        
        data_rub  = poisk(message.text)[2]
        prices = []
        for item in data_rub:
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
                
            data_1  = poisk(message.text)[1]
            
                
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
            bot.send_message(message.chat.id,(
                f'рейтинг:{ReviewRating}\n'
                f'кол-оценок:{Feedbacks}\n'
            ))
            
    else:
        bot.send_message(message.chat.id, 'Нет доступа')

bot.polling(True)
