import telebot

TOKEN = '7471955957:AAFhXEaDb9v3_ZptX1PE-WtdFBu5yteoOIw'

bot = telebot.TeleBot(TOKEN)

keys = {
    'биткоин': 'BTC',
    'эфириум': 'ETH',
    'доллар': 'USD'
}


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = ('Чтобы начать работу введите данные в следующем формате:\n<имя валюты> '
            '<в какую валюту перевести> <количество переводимой валюты>\nУвидеть список доступных валют: /values')
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


bot.polling()
