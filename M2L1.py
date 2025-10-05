#with open('textlesson.txt', 'w', encoding='utf-8') as file:
#   file.write('Привет, Python')
import telebot
import os
import random
import requests
print(os.listdir('images'))
# Инициализация бота с использованием его токена
bot = telebot.TeleBot("вускуе")
@bot.message_handler(commands=['photo'])
def send_my_photo(message):
    img_name=os.listdir('images')
    with open(f'images/{random.choice(img_name)}', 'rb') as f:
        bot.send_photo(message.chat.id, f)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.message_handler(commands=['duck'])
def duck(message):
    '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
    image_url = get_duck_image_url()
    bot.send_photo(message.chat.id, image_url)

def get_anime_image_url():    
    url= 'https://kitsu.io/api/edge/anime?filter[text]=tokio'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.message_handler(commands=['anime'])
def anime(message):
    '''По команде anime вызывает функцию get_anime_image_url и отправляет URL изображения'''
    image_url1 = get_anime_image_url()
    bot.send_photo(message.chat.id, image_url1)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')
# Запуск бота

bot.polling()
