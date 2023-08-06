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
        sendMessage(chat_id, "Ya, I am Online. Send me a Prompt")
    else:
        BASE_URL = "https://lexica.art/api/v1/search?q=" + str(inputText)
        response = requests.get(BASE_URL)
        response_text = json.loads(response.text)
        allImages = response_text["images"]
        sendMediaGroup(chat_id, allImages)
    return Response("ok", status=200)
"""
import telebot
from flask import Flask, request

TOKEN = "6457745689:AAGK_N4F-8KPw7zpnGf8NfFZrpTD2RhkotM"
bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@bot.message_handler(commands=["start"])
def start(message):
    print("Received start command:", message)
    bot.send_message(message.chat.id, "Hello!")


#@app.route('/{}'.format(TOKEN), methods=['POST'])
@app.post("/")
def handle_webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "OK", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url="https://serverless-telegram-bot.vercel.app/" + TOKEN)
    return "Webhook successfully set up"

