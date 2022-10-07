# 🚨 Не меняйте код вне зеленой зоны!
import requests
import json

response = requests.get('https://api.coinbase.com/v2/prices/spot?currency=USD')
data = json.loads(response.text)

# 🟢 (НАЧАЛО) Напишите ваш код здесь 👇

# 🟢 (КОНЕЦ)
