import telebot

TOKEN = "7244782191:AAFlKGTM5C_HY8CKH_R66uRW1zgbrpjExzv5I"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', ])
def send_welcome(message):
    bot.send_message(message.chat.id, f"Добро пожаловать, {message.chat.username} !")


# Обрабатываются все сообщения, содержащие команды '/start' or '/help'
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    bot.reply_to(message, f"Приветствую, {message.chat.username} ")


# Обрабатывается все документы и аудиозаписи
@bot.message_handler(commands=['document', 'audio'])
def handle_docs_audio(message):
    pass


@bot.message_handler(content_types=['voice', ])
def function_name(message: telebot.types.Message):
    bot.send_message(message.chat.id, "У тебя приятный голос!")


@bot.message_handler(content_types=['photo', ])
def say_lmao(message: telebot.types.Message):
    bot.reply_to(message, 'Nice meme XDD')


bot.polling(none_stop=True)
