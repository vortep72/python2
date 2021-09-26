from pprint import pprint
# Внимание! Библиотеку requests нужно установить, выполните в консоли команду:
# pip install requests
import requests
date = '2021/03/25'
url = f'https://www.cbr-xml-daily.ru/archive/{date}/daily_json.js'
# Отправляем запрос на указанный url
response = requests.get(url)
pprint(response.json()['Valute']['USD']['Value'])
pprint(response.json()['Valute']['EUR']['Value'])

# Если хотим получить курсы на определенную дату, то нужно отправить запрос на :
# url: https://www.cbr-xml-daily.ru/archive/2021/04/07/daily_json.js
# где /2021(год)/04(месяц)/07(день)/