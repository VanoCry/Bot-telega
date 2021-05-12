import telebot
from telebot import types
import random
import password

def generator(a):
    password = ""
    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
    for i in range(a):
        password += random.choice(chars)
    return(password)

bot = telebot.TeleBot('1782656960:AAHBZ7dYYSRz2fmPoYhHmCQI4K_mCpw7vEg')
#начальный экран
item1 = types.KeyboardButton('💎Гемы💎')###(не прописана оплата по киви и кейс для 2000)
item2 = types.KeyboardButton('🔥Бесплатно🔥')###
item3 = types.KeyboardButton('🎒Кейсы🎒')
item4 = types.KeyboardButton('⭐️Отзывы⭐️')###
item5 = types.KeyboardButton('❓Как это\nработает?❓')###
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
        akks = types.KeyboardButton('🤔Откуда столько\nаккаунтов?🤔')
        gemz = types.KeyboardButton('🧐Как забрать\nкупленные гемы?🧐')
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
        bot.send_message(message.chat.id, "Сейчас проходят небольшие 🤩скидки(-15%)🤩 И вот наш лист 💎донатов💎 которые вы можете у нас купить🧐:", reply_markup=markup)
        gems_png = open('gems.tgs', 'rb')
        bot.send_message(message.chat.id, "💎30 гемов💎 (45₽) - 15% = 38₽ (Вместо 179₽)\n💎80 гемов💎 (90₽) - 15% = 76₽ (Вместо 449₽)\n💎170 гемов💎 (120₽) - 15% = 102₽ (Вместо 899₽)\n💎360 гемов💎 (199₽) - 15% = 169₽ (Вместо 1790₽)\n💎950 гемов💎 (569₽) - 15% = 483₽ (Вместо 4690₽)\n🎒2000 гемов🎒 возможно получить только из кейса ****")
        bot.send_sticker(message.chat.id, gems_png)
    if message.text == 'Оплатить':
        markup.add(itemback)
        bot.send_message(message.chat.id, "Оплатить покупку можно по Qiwi:\n*номер*\n(введите код сверху👆👆👆 в поле комментария платежа)", reply_markup=markup )
        bot.send_message(message.chat.id, "😄Если вдруг захочешь воспользоваться нашими услугами, ☺️удели время чтобы написать отзыв ему 👉@ioneforever07, ты поможешь развиться нашему проекту😉Спасибо🙂")
    if message.text == '😄Гемы хочу😄':
        markup.add(itemback)
        bot.send_message(message.chat.id, "Для того чтобы БЕСПЛАТНО ПОЛУЧИТЬ 80 ГЕМОВ придётся ПОСТАРАТЬСЯ!😉\nСКОПИРУЙ ЭТО СООБЩЕНИЕ 👇👇👇 И ОТПРАВЬ 30 ДРУЗЬЯМ😜\n(только телеграмм)", reply_markup=markup)
        bot.send_message(message.chat.id, "🎒🎒🎒🎒🎒🎒🎒🎒\n🧐Я КУПИЛ ГЕМЫ ДЕШЕВЛЕ В 3 РАЗА ЧЕРЕЗ ЭТОГО БОТА🧐👇👇👇\n@gemspatrick_bot\n@gemspatrick_bot\n@gemspatrick_bot\n🤫И АККАУНТ ПОЛУЧИЛ В ПОДАРОК🤫\n🎒🎒🎒🎒🎒🎒🎒🎒", reply_markup=markup)
        bot.send_message(message.chat.id, "Скопировал? СКРИНЬ все сообщения и БЕГОМ в мою личку за гемами\n@ioneforever07👈", reply_markup=markup)
        pod_png = open('Wish_pod.tgs', 'rb')
        bot.send_sticker(message.chat.id, pod_png)
    if message.text == '🤔80 Гемов бесплатно🤔':
        markup.add(itemback)
        bot.send_message(message.chat.id, "Для того чтобы БЕСПЛАТНО ПОЛУЧИТЬ 80 ГЕМОВ придётся ПОСТАРАТЬСЯ!😉\nСКОПИРУЙ ЭТО СООБЩЕНИЕ И ОТПРАВЬ 30 ДРУЗЬЯМ😜\n(только телеграмм)", reply_markup=markup)
        bot.send_message(message.chat.id, "🎒🎒🎒🎒🎒🎒🎒🎒\n🧐Я КУПИЛ ГЕМЫ ДЕШЕВЛЕ В 3 РАЗА ЧЕРЕЗ ЭТОГО БОТА🧐👇👇👇\n@gemspatrick_bot\n@gemspatrick_bot\n@gemspatrick_bot\n🤫И 80 ГЕМОВ ПОЛУЧИЛ В ПОДАРОК🤫\n🎒🎒🎒🎒🎒🎒🎒🎒", reply_markup=markup)
        bot.send_message(message.chat.id, "Скопировал? СКРИНЬ все сообщения и БЕГОМ в мою личку за гемами\n@ioneforever07👈", reply_markup=markup)
    if message.text == '💎30 Гемов💎':
        markup.add(itembuy)
        markup.add(itemback)
        gem30 = open('static\gem30.jpg', 'rb')
        bot.send_photo(message.chat.id, gem30)
        bot.send_message(message.chat.id, "Ваша покупка:\n----------------------------------------\n💎30 Гемов💎 за 38₽\n----------------------------------------\nВведите при оплате в поле комментария: " + generator(15), reply_markup=markup)
    if message.text == '💎80 Гемов💎':
        markup.add(itembuy)
        markup.add(itemback)
        gem80 = open('static\gem80.jpg', 'rb')
        bot.send_photo(message.chat.id, gem80)
        bot.send_message(message.chat.id, "Ваша покупка:\n----------------------------------------\n💎80 Гемов💎 за 76₽\n----------------------------------------\nВведите при оплате в поле комментария: " + generator(16), reply_markup=markup)
    if message.text == '💎170 Гемов💎':
        markup.add(itembuy)
        markup.add(itemback)
        gem170 = open('static\gem170.jpg', 'rb')
        bot.send_photo(message.chat.id, gem170)
        bot.send_message(message.chat.id, "Ваша покупка:\n----------------------------------------\n💎170 Гемов💎 за 102₽\n----------------------------------------\nВведите при оплате в поле комментария: " + generator(17), reply_markup=markup)
    if message.text == '💎360 Гемов💎':
        markup.add(itembuy)
        markup.add(itemback)
        gem360 = open('static\gem360.jpg', 'rb')
        bot.send_photo(message.chat.id, gem360)
        bot.send_message(message.chat.id, "Ваша покупка:\n----------------------------------------\n💎360 Гемов💎 за 169₽\n----------------------------------------\nВведите при оплате в поле комментария: " + generator(14), reply_markup=markup)
    if message.text == '💎950 Гемов💎':
        markup.add(itembuy)
        markup.add(itemback)
        gem950 = open('static\gem950.jpg', 'rb')
        bot.send_photo(message.chat.id, gem950)
        bot.send_message(message.chat.id,"Ваша покупка:\n----------------------------------------\n💎950 Гемов💎 за 483₽\n----------------------------------------\nВведите при оплате в поле комментария: "+ generator(18), reply_markup=markup)
    if message.text == '🙃Аккаунт хочу🙃':
        bot.send_message(message.chat.id, "🎆Характеристики аккаунта🎆:\n🏆Кубков: 22111\n💪Бойцов: 43/43\n⚡Леги: Спайк, Ворон, Леон, Сэнди\n⭐Звездные силы: у всех\n💎Гемы: 25\n✔Доступна смена ника\n✔Привязан к Supercell ID\n✔Доступна перепривязка аккаунта")
        imgakk1 = open('imgakk1.jpg', 'rb')
        imgakk2 = open('imgakk2.jpg', 'rb')
        imgakk3 = open('imgakk3.jpg', 'rb')
        bot.send_photo(message.chat.id, imgakk1)
        bot.send_photo(message.chat.id, imgakk2)
        bot.send_photo(message.chat.id, imgakk3)
        bot.send_message(message.chat.id, "❗️❗️❗️ТАКИХ АККАУНТОВ ДЛЯ РАЗДАЧИ ВСЕГО 7❗️❗️❗️\nВсе они чуть разные, но, количество 🏆трофеев и 🔱легендарок одинаковое😎")
        bot.send_message(message.chat.id, "Аккаунт получить чуть ЛЕГЧЕ.\nСКОПИРУЙ ЭТО СООБЩЕНИЕ 👇\nИ ОТПРАВЬ 20 ДРУЗЬЯМ😉\n(только телеграмм)")
        bot.send_message(message.chat.id, "🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁\n🧐Я КУПИЛ ГЕМЫ ДЕШЕВЛЕ В 3 РАЗА ЧЕРЕЗ ЭТОГО БОТА🧐👇👇👇\n@gemspatrick_bot\n@gemspatrick_bot\n@gemspatrick_bot\n🤫И АККАУНТ ПОЛУЧИЛ В ПОДАРОК🤫\n🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁🎁")
        bot.send_message(message.chat.id, "Скопировал? СКРИНЬ все сообщения и БЕГОМ в мою личку за аккаунтом\n@ioneforever07👈", reply_markup=markup)
        pod_png = open('Duck_pod.tgs', 'rb')
        bot.send_sticker(message.chat.id, pod_png)
    if message.text == '🧐Как забрать\nкупленные гемы?🧐':
        markup.add(itemback)
        bot.send_message(message.chat.id, "♦После оплаты с указанным кодом в комментариях платежа♦\nТебе приходит код который нужно ввести в поле 'КОД АВТОРА' и ты получишь свой товар😉", reply_markup=markup )
        ok_png = open('ok.webp', 'rb')
        bot.send_sticker(message.chat.id, ok_png, reply_markup=markup)
    if message.text == '🤔Откуда столько\nаккаунтов?🤔':
        markup.add(itemback)
        bot.send_message(message.chat.id, "Бот подключен к бирже аккаунтов, где скупает 'мёртвые' аккаунты(аккаунты на которые давно никто не заходил) Вскоре админ прокачивает эти аккаунты и часть уходит на продажу, а часть меняется на 💎'гемные'💎 коды, которые потом продаёт этот бот☺", reply_markup=markup )
        duck_png = open('duck.tgs', 'rb')
        bot.send_sticker(message.chat.id, duck_png, reply_markup=markup)


bot.polling(none_stop=True)
