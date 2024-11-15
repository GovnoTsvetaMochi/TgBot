import telebot
from telebot import types
from urllib.request import urlopen

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Работа с нами")
    btn2 = types.KeyboardButton("Оформить карту")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Здравстуйте, {0.first_name}!"
                          " Здесь вы можете оформить себе карту со стартовым капиталом.".format(message.from_user),
                     reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    markupp = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == "Работа с нами":
        btntest = types.KeyboardButton("Работаем")
        markupp.add(btntest)
        bot.send_message(message.chat.id, text="🔥Мы рекламное агентство в Банковской сфере\n"
                                               "Сайт с описанием и отзывами - https://vk.com/worki2025\n"
                                               "💬Вы лично можете пообщаться с любым "
                                               "пользователем, как гарантом исполнения наших обязательств\n", reply_markup=markupp)

    elif message.text == "Работаем":
        btntest1 = types.KeyboardButton("Далее")
        markupp.add(btntest1)
        bot.send_message(message.chat.id, text="Каждому положена выплата от банка (Успевайте) 👇👇\n"
                                               "📍 Суть подработки:\n"
                                               "Вы оформляйте бесплатные продукты банка, по нашей реферальной "
                                               "программе.\n"
                                               "— Для вас это подработка, дополнительный заработок.\n"
                                               "— После получения выплаты, любую из бесплатных карт можно закрыть "
                                               "через приложение, это не кредит.\n"
                                               "— Вы ничем не рискуйте и никаких вложений.\n"
                                               "Банки платят ₽ что бы вы завели их дебетовую карту\n"
                                               "🏛Банк 👉 Мы 💶 👉 Вы\n"
                                               "Оплата сразу в день получения любой из карт, переводом!\n"
                                               "Вы получайте оплату от 500₽ - 10 000₽, переводом на любой банк, "
                                               "в зависимости от кол-ва выполненных заданий.\n"
                                               "❗ Обращаем внимание, только культурное общение❗\n"
                                               "Выплаты проводятся ежедневно, с 14:00 - 18:00 по мск!\n"
                                               "✅ Легальная подработка по реферальной программе известных банков!\n",
                         reply_markup=markupp)

    elif message.text == "Далее":
        btntest2 = types.KeyboardButton("Получить задание")
        markupp.add(btntest2)
        bot.send_message(message.chat.id, text="📲⚒Что необходимо делать:\n"
                                               "Заказывать по нашим ссылкам бесплатные дебетовые карты;\n"
                                               "Активировать карты, сообщать нам - получать вознаграждение;\n"
                                               "💡 Правильно ли я вас понял, вы готовы начать? Для вас подобраны "
                                               "первые задания\n", reply_markup=markupp)
    elif message.text == "Получить задание":
        photo_url1 = ('https://moneyman.ru/wp-content/uploads/2020/06/Geograficheskie-ogranicheniya-po-kartam'
                      '-Gazprombanka.jpg')
        photo_url2 = 'https://cdn.viberu.ru/help/zzqkxg0452g.jpg'
        photo_url3 = 'https://api-reforum.banki.ru/reforum/c4/10/31/7c/2d/sc5p16c43e83eea7.jpg'
        text = '[Оформить сейчас](https://clck.ru/3E6XFY)'
        text2 = '[Оформить сейчас](https://clck.ru/3E9dgR)'
        text3 = '[Оформить сейчас](https://clck.ru/3E9drk)'
        back1 = types.KeyboardButton("Меню")
        markupp.add(back1)
        bot.send_photo(message.chat.id, urlopen(photo_url1),

                       'Кэшбэк 35%\\ на всё самое важное\n'

                       '🆓 Бесплатно выпуск, обслуживание, доставка\n'

                       'До 5 000 кэшбэк\n каждый месяц\n'

                       '35%\\ кэшбэк на топовые категории\n с 1 августа 2024 по 31 января 2025\n'
                       '🏷️Маркетплейсы и супермаркеты\n'
                       '🏷️Кафе, рестораны и фастфуд\n'
                       '🏷️Одежда и обувь\n'
                       '🏷️Такси, общественный транспорт и АЗС\n'
                       '🏷️ЖКХ и Госуслуги «штрафы и налоги»\n'
                       'Подтвердите участие в приложении/интернет—банке в разделе «Кэшбэк баллами» до 31 января 2025\nМинимальные траты — 5 000 ₽ в месяц\n'
                       + f"*{text}*",

                       parse_mode='MarkdownV2', reply_markup=markupp)

        bot.send_photo(message.chat.id, urlopen(photo_url2),

                       '💳 Первая дебетовая карта со скидкой везде\n'

                       'Бесплатный выпуск\n'

                       'Скидка до 10 000 ₽ каждый месяц\n'

                       '🪙 До 19%\\ годовых на ежедневный остаток по МТС Счёту\n'

                       '🛍️ Скидка\n'
                       '1%\\ — на любые покупки\n'
                       '3%\\*\\ — на покупки в интернете первые два месяца и\n'
                       'дальше при совершении 25 покупок за предыдущий месяц, а также для зарплатных клиентов\n'
                       'доступно только для первой карты Скидка везде с лояльностью «Скидка»\n'
                       'Максимальный размер скидки\n'
                       '10 000 ₽/мес\n'
                       'Кешбэк бонусами с подпиской МТС Premium\n'
                       '5% в супермаркетах\n'
                       + f"*{text2}*",parse_mode='MarkdownV2', reply_markup=markupp)

        bot.send_photo(message.chat.id, urlopen(photo_url3),

                       '🪙 Повышенный кэшбэк\n'

                       'До 30% у партнеров и до 15% в выбранных категориях и местах\n'

                       '🔥 0 ₽ за обслуживание\n'

                       '💰 Кэшбэк рублями, а не бонусами\n'

                       'До 30% у партнеров, до 15% в категории «Развлечения», 10% — «Музыка», 7% — «Фастфуд» в первый месяц\n'

                       '🆓 Снятие без комиссии\n'

                       'До 500 000 ₽ в банкоматах Т‑Банка, от 3000 до 100 000 ₽ в других банкоматах\n' + f"*{text3}*",parse_mode='MarkdownV2', reply_markup=markupp)


    elif message.text == "Оформить карту":

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Газпромбанк")
        btn2 = types.KeyboardButton("МТС банк")
        btn3 = types.KeyboardButton("Тинькофф")
        back = types.KeyboardButton("Меню")
        markup.add(btn1, btn2, btn3, back)
        bot.send_message(message.chat.id, text="Выбери Банк", reply_markup=markup)


    elif message.text == "Газпромбанк":

        text = '[Оформить сейчас](https://clck.ru/3E6XFY)'

        photo_url = 'https://moneyman.ru/wp-content/uploads/2020/06/Geograficheskie-ogranicheniya-po-kartam-Gazprombanka.jpg'

        bot.send_photo(message.chat.id, urlopen(photo_url),

                       'Кэшбэк 35%\\ на всё самое важное\n'

                       '🆓 Бесплатно выпуск, обслуживание, доставка\n'

                       'До 5 000 кэшбэк каждый месяц\n'

                       '35%\\ кэшбэк на топовые категории с 1 августа 2024 по 31 января 2025\n' + f"*{text}*",

                       parse_mode='MarkdownV2', reply_markup=markupp)


    elif message.text == "МТС банк":

        text2 = '[Оформить сейчас](https://clck.ru/3E9dgR)'

        photo_url = 'https://cdn.viberu.ru/help/zzqkxg0452g.jpg'

        bot.send_photo(message.chat.id, urlopen(photo_url),

                       '💳 Первая дебетовая карта со скидкой везде\n'

                       'Бесплатный выпуск\n'

                       'Скидка до 10 000 ₽ каждый месяц\n'

                       '🪙 До 19%\\ годовых на ежедневный остаток по МТС Счёту\n'

                       '🛍️ Скидка\n' + f"*{text2}*",

                       parse_mode='MarkdownV2', reply_markup=markupp)


    elif message.text == "Тинькофф":

        text3 = '[Оформить сейчас](https://clck.ru/3E9drk)'

        photo_url = 'https://api-reforum.banki.ru/reforum/c4/10/31/7c/2d/sc5p16c43e83eea7.jpg'

        bot.send_photo(message.chat.id, urlopen(photo_url),

                       '🪙 Повышенный кэшбэк\n'

                       'До 30% у партнеров и до 15% в выбранных категориях и местах\n'

                       '🔥 0 ₽ за обслуживание\n'

                       '💰 Кэшбэк рублями, а не бонусами\n'

                       'До 30% у партнеров, до 15% в категории «Развлечения», 10% — «Музыка», 7% — «Фастфуд» в первый месяц\n'

                       '🆓 Снятие без комиссии\n'

                       'До 500 000 ₽ в банкоматах Т‑Банка, от 3000 до 100 000 ₽ в других банкоматах\n' + f"*{text3}*",

                       parse_mode='MarkdownV2', reply_markup=markupp)
    elif message.text == "Меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Работа с нами")
        button2 = types.KeyboardButton("Оформить карту")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммировал..")

    print(str(message.from_user) +' пишет: ' +message.text)
    log = open('C:/Users/Толик-еболик/Desktop/TgbotLog/log.txt', 'a')
    log.write(str(message.from_user) + ' Написал: '+ message.text + '\n')

bot.infinity_polling()
bot.polling()