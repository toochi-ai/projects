import json

import requests
import telebot

TOKEN = '7471955957:AAFhXEaDb9v3_ZptX1PE-WtdFBu5yteoOIw'

bot = telebot.TeleBot(TOKEN)

keys = {
    'биткоин': 'BTC',
    'эфириум': 'ETH',
    'доллар': 'USD'
}


class ConvertionException(Exception):
    pass


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = ('Чтобы начать работу введите данные в следующем формате:\n<имя валюты> '
            '<в какую валюту перевести> <количество переводимой валюты>\nУвидеть список доступных валют: /values')
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    values = message.text.split(' ')

    if len(values) > 3:
        raise ConvertionException('Слишком много параметров.')

    quote, base, amount = values

    if quote == base:
        raise ConvertionException(f'Невозможно конвертировать одинаковые валюты {base}.')

    try:
        quote_ticker = keys[quote]
    except KeyError:
        raise ConvertionException(f'Не удалось выбрать валюту {quote}')

    try:
        base_ticker = keys[base]
    except KeyError:
        raise ConvertionException(f'Не удалось выбрать валюту {base}')

    try:
        amount = float(amount)
    except ValueError:
        raise ConvertionException(f'Не удалось обработать количество {amount}.')

    r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
    total_base = json.loads(r.content)[keys[base]]
    text = f'Цена {amount} {quote} в {base} - {total_base}'
    bot.send_message(message.chat.id, text)


bot.polling()
