import telebot
import os
import bot_logic
import requests
import random

bot = telebot.TeleBot("7984070993:AAF-bsOgEq-SwuuBIMYuO_W97afd2yYHDdM")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}! Напиши /help, чтобы узнать больше!')
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
@bot.message_handler(commands=['categories'])
def send_categories(message):
    bot.reply_to(message, "Вот категории мусора, про которые могу рассказать! Glass, paper, plastic, metal")
    with open('images/categories.jpg', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Вот список моих команд! \n/start - запуск бота, \n/help - список команд, \n/hello - поздороваться, \n/categories - категории вещей для сдачи, \n/glass - информация про стекло, \n/paper - информация про бумагу, \n/plastic - информация про пластик, \n/metal - информация про металл")

@bot.message_handler(commands=['glass'])
def send_glass(message):
    bot.reply_to(message, "Отсортируй по цвету(цветной/прозрачный) и можешь смело сдавать промытую стеклотару и битое стекло.")
    with open('images/glass.jpg', 'rb') as f:
        bot.send_photo(message.chat.id, f)
@bot.message_handler(commands=['paper'])
def send_glass(message):
    bot.reply_to(message, "В переработку тетради и книги, можешь газеты и картон захватить.")
    with open('images/paper.jpg', 'rb') as f:
        bot.send_photo(message.chat.id, f)
@bot.message_handler(commands=['plastic'])
def send_plastic(message):
    bot.reply_to(message, "Отсортируй по цвету маркировке и можешь смело сдавать пластик.")
    with open('images/plastic.jpg', 'rb') as f:
        bot.send_photo(message.chat.id, f)
@bot.message_handler(commands=['metal'])
def send_metal(message):
    bot.reply_to(message, "Удали все неметаллические части и можешь сдавать в пункты приема.")
    with open('images/metal.jpg', 'rb') as f:
        bot.send_photo(message.chat.id, f)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
