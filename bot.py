import os
import requests

BOT_TOKEN = os.environ['8772491308:AAFj70yPKMoRXqKqTn2nlwdqM69UouUNzTg'
]
CHAT_ID = os.environ['8622741736']

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
requests.post(url, data={"chat_id": CHAT_ID, "text": "🔥 BOT WORKING SUCCESS"})
