import telebot
bot = telebot.TeleBot('6805436974:AAEMlhr-0lPYHNk5DK76e3yywNzKJ64Br9U')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет! Это бот поэт')

@bot.message_handler(commands=['pushkin'])
def main(message):
    bot.send_message(message.chat.id, 'Мороз и солнце, день чудесный')


@bot.message_handler(commands=['lermontov'])
def main(message):
    bot.send_message(message.chat.id, 'Белеет парус одинокий \nВ тумане моря голубом')


@bot.message_handler(commands=['yesenin'])
def main(message):
    bot.send_message(message.chat.id, '_Гой ты, Русь, моя родная_', parse_mode='Markdown')

bot.infinity_polling()