import config
import telebot
import phrases 

bot = telebot.TeleBot(config.token)
from telebot import types


@bot.message_handler(commands=['start'])
    
def start(message):
 #   markup = types.ReplyKeyboardMarkup()
 #   buttonA = types.KeyboardButton('A')
 #   buttonB = types.KeyboardButton('B')
 #   buttonC = types.KeyboardButton('C')

 #   markup.row(buttonA, buttonB)
 #   markup.row(buttonC)
    greetings = '''Привет, я умею:\n
    -отвечать на приветствия\n
    -отвечать на вопросы как у тебя дела\n
    -рассказывать анекдоты\n
    -отвечать на фото, аудио, видео и стикеры рандомными стикерами\n
    -на вопрос о погоде давать точный прогноз погоды в Москве на завтрашний день'''
    bot.send_message(message.chat.id, greetings)

@bot.message_handler(content_types='text')
def text_messages(message):
    msg = message.text.lower()
    if msg.count('прив') or msg.count('здаров'):
        bot.send_message(message.from_user.id, phrases.hello())
    elif msg.count('как дела') or msg.count('как поживаешь'):
        bot.send_message(message.from_user.id, phrases.how_are_you())
    elif msg.count('анекдот') or msg.count('шутк'):
        bot.send_message(message.from_user.id, phrases.jokes())
    elif msg.count('погод'):
        bot.send_message(message.from_user.id, phrases.weather())
    else:
        bot.send_message(message.from_user.id, phrases.not_understand())


@bot.message_handler(content_types=['audio', 'video', 'document', 'location', 'sticker'])
def media_messages(message):
    bot.send_sticker(message.from_user.id, phrases.sticker_id())


if __name__ == '__main__':
    bot.infinity_polling()