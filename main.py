import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import requests


TOKEN = "5958081967:AAFSDhG4CshOZqHKCIq9VFzQ-fJnHNuBjqg"

bot = telebot.TeleBot(token=TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def welcome_message(message):
    welcome_message = "Привет. Этот бот достает фотки кошек  из интернета!"

    bot.reply_to(message, welcome_message, reply_markup=keyboard())

@bot.message_handler(content_types=['text'])
def message_handle(message):
    if message.text == "Дай кота!":
        cat = get_cat()
        bot.send_photo(message.chat.id, cat)

def keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

    button1 = KeyboardButton("Дай кота!")
    keyboard.add(button1)

    return keyboard

def get_cat():

    zagalovki = {"content-type": "image/jpeg"}
    reply = requests.get("https://thiscatdoesnotexist.com/", headers=zagalovki)

    image = reply.content
    return image

bot.infinity_polling()