import requests
import telebot

def poisk(mass):
    mass=mass.replace(" ", "")
    ochenk_url=f'https://card.wb.ru/cards/v2/detail?appType=1&curr=kzt&dest=269&spp=30&hide_dtype=10%3B13%3B14&ab_testing=false&lang=ru&nm={mass}'
    base_url = f"https://alm-basket-cdn-02.geobasket.ru/vol{mass[0:4]}/part{mass[0:6]}/{mass}"
    info_url = f"{base_url}/info/ru/card.json"

    price_url = f"{base_url}/info/price-history.json"
     
    try:
        response_3=requests.get(ochenk_url)
        response_2 = requests.get(price_url)
        response = requests.get(info_url)
        if response.status_code and response_2.status_code == 200:
            return True, response.json(),response_2.json(),response_3.json()
        else:
            return False,None,response.status_code
    except Exception as e:
        return f"Ошибка запроса: {e}"