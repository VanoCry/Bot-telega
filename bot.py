import telebot
from telebot import types
import random
import password



bot = telebot.TeleBot('1782656960:AAHBZ7dYYSRz2fmPoYhHmCQI4K_mCpw7vEg')
#начальный экран
item1 = types.KeyboardButton('💎Гемы💎')#
item2 = types.KeyboardButton('🔥Бесплатно🔥')##
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

#ОСНОВА ПЕРЕМЕЩЕНИЙ
@bot.message_handler(content_types =['text'])
def lalala(message):
    #ПРИКРУТИЛ КНОПКУ НАЗАД СЮДА
    itemback = types.KeyboardButton('Назад')
    itembuy = types.KeyboardButton('Оплатить')
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
    if message.text == '💎Гемы💎':
        i30 = types.KeyboardButton('💎30 Гемов💎')
        i30 = types.KeyboardButton('💎30 Гемов💎')
        i30 = types.KeyboardButton('💎30 Гемов💎')
        i80 = types.KeyboardButton('💎80 Гемов💎')
        i170 = types.KeyboardButton('💎170 Гемов💎')
        i360 = types.KeyboardButton('💎360 Гемов💎')
        i950 = types.KeyboardButton('💎950 Гемов💎')
        i2000 = types.KeyboardButton('🎒2000 Гемов🎒')
        ifree80 = types.KeyboardButton('🤔80 Гемов бесплатно🤔')
        markup.add(i30,i80)
        markup.add(i170,i360)
        markup.add(i950,i2000)
        markup.add(ifree80)
        markup.add(itemback)
        bot.send_message(message.chat.id, "Сейчас проходят небольшие 🤩скидки(-15%)🤩 И вот наш лист 💎донатов💎 которые вы можете у нас купить🧐:")
        gems_png = open('gems.tgs', 'rb')
        bot.send_sticker(message.chat.id, gems_png)
        bot.send_message(message.chat.id, "список", reply_markup=markup)
    if message.text == 'Оплатить':
        markup.add(itemback)
        bot.send_message(message.chat.id, "Оплатить покупку можно по Qiwi:\n*номер*\n(введите код сверху👆👆👆 в поле комментария платежа)\n (Другие способы оплаты доступны у менеджера @ioneforever07)", reply_markup=markup )
    if message.text == '😄Гемы хочу😄':
        markup.add(itemback)
        bot.send_message(message.chat.id, "Для того чтобы БЕСПЛАТНО ПОЛУЧИТЬ 80 ГЕМОВ придётся ПОСТАРАТЬСЯ!😉\nСКОПИРУЙ ЭТО СООБЩЕНИЕ И ОТПРАВЬ 30 ДРУЗЬЯМ😜\n(только телеграмм)", reply_markup=markup)
        bot.send_message(message.chat.id, "🎒🎒🎒🎒🎒🎒🎒🎒\n🧐Я КУПИЛ ГЕМЫ ДЕШЕВЛЕ В 3 РАЗА ЧЕРЕЗ ЭТОГО БОТА🧐👇👇👇\n@gemspatrick_bot\n@gemspatrick_bot\n@gemspatrick_bot\n🤫И 80 ГЕМОВ ПОЛУЧИЛ В ПОДАРОК🤫\n🎒🎒🎒🎒🎒🎒🎒🎒", reply_markup=markup)
        bot.send_message(message.chat.id, "Скопировал? СКРИНЬ все сообщения и БЕГОМ в мою личку за гемами\n@ioneforever07👈", reply_markup=markup)
    if message.text == '🤔80 Гемов бесплатно🤔':
        markup.add(itemback)
        bot.send_message(message.chat.id, "Для того чтобы БЕСПЛАТНО ПОЛУЧИТЬ 80 ГЕМОВ придётся ПОСТАРАТЬСЯ!😉\nСКОПИРУЙ ЭТО СООБЩЕНИЕ И ОТПРАВЬ 30 ДРУЗЬЯМ😜\n(только телеграмм)", reply_markup=markup)
        bot.send_message(message.chat.id, "🎒🎒🎒🎒🎒🎒🎒🎒\n🧐Я КУПИЛ ГЕМЫ ДЕШЕВЛЕ В 3 РАЗА ЧЕРЕЗ ЭТОГО БОТА🧐👇👇👇\n@gemspatrick_bot\n@gemspatrick_bot\n@gemspatrick_bot\n🤫И 80 ГЕМОВ ПОЛУЧИЛ В ПОДАРОК🤫\n🎒🎒🎒🎒🎒🎒🎒🎒", reply_markup=markup)
        bot.send_message(message.chat.id, "Скопировал? СКРИНЬ все сообщения и БЕГОМ в мою личку за гемами\n@ioneforever07👈", reply_markup=markup)
    if message.text == '💎30 Гемов💎':
        markup.add(itembuy)
        markup.add(itemback)
        bot.send_message(message.chat.id, "Ваша покупка:\n----------------------------------------\n💎30 Гемов💎 за 38₽\n----------------------------------------\nВведите при оплате в поле комментария:", reply_markup=markup)
    if message.text == '💎80 Гемов💎':
        markup.add(itembuy)
        markup.add(itemback)
        bot.send_message(message.chat.id, "Ваша покупка:\n----------------------------------------\n💎80 Гемов💎 за 76₽\n----------------------------------------\nВведите при оплате в поле комментария:", reply_markup=markup)
    if message.text == '💎170 Гемов💎':
        markup.add(itembuy)
        markup.add(itemback)
        bot.send_message(message.chat.id, "Ваша покупка:\n----------------------------------------\n💎170 Гемов💎 за 102₽\n----------------------------------------\nВведите при оплате в поле комментария:", reply_markup=markup)
    if message.text == '💎360 Гемов💎':
        markup.add(itembuy)
        markup.add(itemback)
        bot.send_message(message.chat.id, "Ваша покупка:\n----------------------------------------\n💎360 Гемов💎 за 169₽\n----------------------------------------\nВведите при оплате в поле комментария:", reply_markup=markup)
    if message.text == '💎950 Гемов💎':
        markup.add(itembuy)
        markup.add(itemback)
        bot.send_message(message.chat.id, "Ваша покупка:\n----------------------------------------\n💎950 Гемов💎 за 483₽\n----------------------------------------\nВведите при оплате в поле комментария:", reply_markup=markup)











bot.polling(none_stop=True)
