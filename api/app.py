from flask import Flask, request
import telebot
from telebot.types import *

TOKEN = "5769907387:AAF0tVVa2RNQjFpOeYmRAIWBhzIBa1jFp4E"
server = Flask(__name__)

bot = telebot.TeleBot(TOKEN, parse_mode="html")

@bot.message_handler(commands=["start"])
def start(message):
	bot.send_message(message.chat.id, "Hi")

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200
    
@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://serverless-telegram-bot1.vercel.app/' + TOKEN)
    return "ok", 200

#if __name__ == "__main__":
    #server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
