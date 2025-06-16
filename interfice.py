from core import *
data_ochenk = poisk(mess)[3]
for i in data_ochenk['data']['products']:
    ReviewRating=i['nmReviewRating']
    Feedbacks=i['nmFeedbacks']
    
            
        
Data_rub  = poisk(mess)[2]
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
                    
                data_1  = poisk(mess)[1]
            
                
    name = data_1["imt_name"]
    brand = data_1["selling"]["brand_name"]
    price = data_1["subj_name"]
    desc = data_1["description"]
                
    msg = f"Название: {name}\nБренд: {brand}\nЦена: {current_price}\nОписание: {desc}"