from flask import Flask, request
import telebot
from telebot.types import *

TOKEN = "6457745689:AAGK_N4F-8KPw7zpnGf8NfFZrpTD2RhkotM"
bot = telebot.TeleBot(TOKEN, parse_mode="html")
app = Flask(__name__)

@bot.message_handler(commands =["start"])
def start(message):
	bot.send_message(message.chat.id, "Hello!")

@app.route('/webhook', methods=['POST'])
def webhook():
     update = telebot.types.Update.de_json(
            request.stream.read().decode("utf-8"))
     bot.process_new_updates([update])
     return "ok", 200
