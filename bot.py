import telebot
from telebot import types
import random
import password

gener = password.gener(1)

bot = telebot.TeleBot('1782656960:AAHBZ7dYYSRz2fmPoYhHmCQI4K_mCpw7vEg')
#начальный экран
item1 = types.KeyboardButton('💎Гемы💎')
item2 = types.KeyboardButton('🔥Бесплатно🔥')#
item3 = types.KeyboardButton('🎒Кейсы🎒')
item4 = types.KeyboardButton('⭐️Отзывы⭐️')###
item5 = types.KeyboardButton('❓Как это\nработает?❓')#
item6 = types.KeyboardButton('🚫не пришёл\nтовар🚫')###
item7 = types.KeyboardButton('🤩аккаунты🤩')
@bot.message_handler(commands=['start'])
def welcome(message):
    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    #менюшка
    markup.add(item1,item3)
    markup.add(item2, item7)
    markup.add(item5, item6)
    markup.add(item4)

    bot.send_message(message.chat.id, "Привет!")
    bot.send_message(message.chat.id, "Выбери что тебе по душе!", reply_markup=markup)
    hello_png = open('AnimatedSticker.tgs', 'rb')
    bot.send_sticker(message.chat.id, hello_png)
#экран закончился

#основа перемещений
@bot.message_handler(content_types =['text'])
def lalala(message):
    #ПРИКРУТИЛ КНОПКУ НАЗАД СЮДА
    itemback = types.KeyboardButton('Назад')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#прикрутил действие к кнопке Отзывов
    if message.text == '⭐️Отзывы⭐️':
        #кнопка назад
        markup.add(itemback)
        #ссылка на отзывы
        keyboard = types.InlineKeyboardMarkup()
        url_btn = types.InlineKeyboardButton(text='💫Отзывы💫', url='https://t.me/otzuvi_gemi')
        keyboard.add(url_btn)
        #стикер звезды в отзывах (к ней прикреплена кнопка)
        star_png = open('Star.tgs', 'rb')
        bot.send_sticker(message.chat.id, star_png, reply_markup=markup)
        #сообщение
        bot.send_message(message.chat.id, "Отзывы ты можешь посмотреть здесь👇👇👇", reply_markup=keyboard )
#возвращение в меню
    if message.text == 'Назад':
        markup.add(item1,item3)
        markup.add(item2, item7)
        markup.add(item5, item6)
        markup.add(item4)
        bot.send_message(message.chat.id, "Выбери что тебе по душе!", reply_markup=markup)

    if message.text == '🚫не пришёл\nтовар🚫':
        markup.add(itemback)
        #сообщения
        bot.send_message(message.chat.id, "Приносим извинения предоставленные неудобства", reply_markup=markup)
        bot.send_message(message.chat.id, "Скорее всего ваш заказ всё ещё обрабатывается. Следует подождать 30 минут")
        #Стикер
        sad_png = open('sad.webp', 'rb')
        bot.send_sticker(message.chat.id, sad_png)
        bot.send_message(message.chat.id, "Если же товар не пришёл через указанное время, срочно пишите нашему менеджеру @ioneforever07 и он разберётся в этой ситуации.")
    if message.text == '🔥Бесплатно🔥':
        #выбор гемы или аккаунт
        freegems = types.KeyboardButton('😄Гемы хочу😄')
        freeakk = types.KeyboardButton('🙃Аккаунт хочу🙃')
        markup.add(freegems, freeakk)
        markup.add(itemback)
        bot.send_message(message.chat.id, "Ну есть у меня бесплатное) а что?)", reply_markup=markup)
    if message.text == '❓Как это\nработает?❓':
        akks = types.KeyboardButton('🤔Откуда столько\nаккаунтов🤔')
        gemz = types.KeyboardButton('🧐Как забрать\nкупленные гемы🧐')
        markup.add(akks, gemz)
        markup.add(itemback)
        quest_png = open('quest.tgs', 'rb')
        bot.send_sticker(message.chat.id, quest_png, reply_markup=markup)

    if message.text == '567':
        bot.send_message(message.chat.id, gener, reply_markup=markup)

    








bot.polling(none_stop=True)
