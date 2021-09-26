import requests


class Currency:
    def __init__(self, type):
        self.type = type.upper()

    def __getitem__(self, date):
        day, month, year = date.split('.')
        url = f'https://www.cbr-xml-daily.ru/archive/{year}/{month}/{day}/daily_json.js'
        response = requests.get(url)

        return response.json()['Valute'][self.type]['Value']


usd = Currency("usd")  # Создаем валюту "Доллар"
euro = Currency("eur")  # Создаем валюту "Евро"
print(usd['02.09.2020'])  # ← получение курса доллара на указанную дату
print(euro['12.10.2018'])  # ← получение курса евро на указанную дату
print(euro['12.12.2018'])  # ← в случае некорректной выбрасываем исключение