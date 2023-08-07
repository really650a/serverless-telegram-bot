"""import os
import json
import requests
from flask import Flask
from flask import request
from flask import Response
import telebot

app = Flask(__name__)
TOKEN = "6457745689:AAGK_N4F-8KPw7zpnGf8NfFZrpTD2RhkotM"

#bot = telebot.TeleBot(TOKEN)

def imageAsDict(imageURL, caption):
    return {
        "type": "photo",
        "media": imageURL,
        "caption": caption,
    }


def sendMediaGroup(chatid, allImages):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMediaGroup"
    media = [imageAsDict(allImages[i]["src"], allImages[i]["prompt"]) for i in range(5)]
    payload = {"chat_id": chatid, "media": media}
    r = requests.post(url, json=payload)
    return r

def sendMessage(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": chat_id, "text": text}
    r = requests.post(url, json=payload)
    return r
"""

"""@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello,')
"""
"""
@app.post("/")
def index():
    msg = request.get_json()
    #update = telebot.types.Update.de_json(msg)
    #bot.process_new_updates([update])
    chat_id = msg["message"]["chat"]["id"]
    inputText = msg["message"]["text"]
    if inputText == "/start":
        #sendMessage(chat_id, msg)
        sendMessage(chat_id, "Ya, I am Online. Send me a Prompt")
    else:
        BASE_URL = "https://lexica.art/api/v1/search?q=" + str(inputText)
        response = requests.get(BASE_URL)
        response_text = json.loads(response.text)
        allImages = response_text["images"]
        sendMediaGroup(chat_id, allImages)
    return Response("ok", status=200)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
"""

from flask import Flask, request
import telebot
from telebot.types import *

TOKEN = "6457745689:AAGK_N4F-8KPw7zpnGf8NfFZrpTD2RhkotM"
bot = telebot.TeleBot(TOKEN, parse_mode="html")
server = Flask(__name__)

@bot.message_handler(commands =["start"])
def start(message):
    bot.send_message(message.chat.id, "Hello!")

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    if update.message:
        bot.process_new_messages([update.message])
    
    return "ok", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://serverless-telegram-fs1wzhlwh-really650a.vercel.app/' + TOKEN)
    return "ok", 200

if __name__ == "__main__":
    server.run(debug=True)

