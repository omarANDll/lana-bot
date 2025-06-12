import telebot

import os
API_TOKEN = os.environ['API_TOKEN']

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "أهلًا! أنا هنا أستمع لك 💬")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"سمعتك تقول: {message.text}")


bot.infinity_polling()
