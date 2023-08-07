"""import os
import json
import requests
from flask import Flask
from flask import request
from flask import Response
import telebot

app = Flask(__name__)
TOKEN = "6457745689:AAGK_N4F-8KPw7zpnGf8NfFZrpTD2RhkotM"

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

@app.post("/")
def index():
    msg = request.get_json()
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
import telebot

TOKEN = '6457745689:AAGK_N4F-8KPw7zpnGf8NfFZrpTD2RhkotM'
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200
