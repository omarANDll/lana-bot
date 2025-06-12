import telebot

API_TOKEN = '7807500247:AAH9kg2ckn9O5B886_1Cihiqq6Ef5wcA5pE'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "أهلًا! أنا هنا أستمع لك 💬")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"سمعتك تقول: {message.text}")


bot.infinity_polling()
