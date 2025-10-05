import os
import telebot

import bot_logic
bot = telebot.TeleBot("'Telebot_secret_cod")

text_messages = {
    'welcome':
        u'Please welcome {name}!\n\n'
        u'I am a bot that assists this channel'
        u'I hope you enjoy your stay here!'
}
@bot.message_handler(commands=['password'])
def send_password(message):
    bot.send_message(message.chat.id, bot_logic.gen_pass(10))
@bot.message_handler(commands=['flip'])
def send_flip(message):
    bot.send_message(message.chat.id, bot_logic.flip_coin())
@bot.message_handler(commands=['emodji'])
def send_emodji(message):
    bot.send_message(message.chat.id, bot_logic.gen_emodji())

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")
# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)
#Проверка на жизнь
@bot.message_handler(commands=["ping"])
def on_ping(message):
    bot.reply_to(message, "Still alive and kicking!")

#Вступление новых в группу
if "TELEBOT_BOT_TOKEN" not in os.environ or "GROUP_CHAT_ID" not in os.environ:
    raise AssertionError("Please configure TELEBOT_BOT_TOKEN and GROUP_CHAT_ID as environment variables")

bot = telebot.AsyncTeleBot(os.environ["TELEBOT_BOT_TOKEN"])
GROUP_CHAT_ID = int(os.environ["GROUP_CHAT_ID"])
def is_api_group(chat_id):
    return chat_id == GROUP_CHAT_ID

@bot.message_handler(func=lambda m: True, content_types=['new_chat_participant'])
def on_user_joins(message):
    if not is_api_group(message.chat.id):
        return

    name = message.new_chat_participant.first_name
    if hasattr(message.new_chat_participant, 'last_name') and message.new_chat_participant.last_name is not None:
        name += u" {}".format(message.new_chat_participant.last_name)

    if hasattr(message.new_chat_participant, 'username') and message.new_chat_participant.username is not None:
        name += u" (@{})".format(message.new_chat_participant.username)

    bot.reply_to(message, text_messages['welcome'].format(name=name))

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
bot.polling()