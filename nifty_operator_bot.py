import os
import requests
from datetime import datetime
import yfinance as yf

BOT_TOKEN = os.environ['BOT_TOKEN']
CHAT_ID = os.environ['CHAT_ID']

def get_signal():
    data = yf.Ticker("^NSEI").history(period="2d")
    close = data["Close"].iloc[-1]
    prev = data["Close"].iloc[-2]

    high = data["High"].iloc[-1]
    low = data["Low"].iloc[-1]
    vwap = (high + low + close)/3

    trend = "UP" if close > prev else "DOWN"

    if close > vwap and trend == "UP":
        return "BUY CE 🟢"
    elif close < vwap and trend == "DOWN":
        return "BUY PE 🔴"
    else:
        return "WAIT ⚫"

def send():
    signal = get_signal()
    msg = f"""🔥 NIFTY SIGNAL

Time: {datetime.now()}

Signal: {signal}
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

send()
