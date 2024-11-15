import telebot
from telebot import types
from urllib.request import urlopen

bot = telebot.TeleBot('7425211006:AAHBZYAR_1_OXG8KycPQ06KUBWY8LcaGvl4')

@bot.message_handler(commands=['start'])
def handle_start(message):
  # Создание клавиатуры
  keyboard = types.ReplyKeyboardMarkup(row_width=2)
  button1 = types.KeyboardButton('Газпромбанк')
  button2 = types.KeyboardButton('МТС банк')
  button3 = types.KeyboardButton('Тинькофф')
  keyboard.add(button1, button2, button3)

  # Отправка сообщения с клавиатурой
  bot.reply_to(message, 'Здесь вы можете оформить себе карту.', reply_markup=keyboard)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
  if message.text == 'Газпромбанк':
      # Действия при нажатии на кнопку 1
      photo1 = urlopen('https://moneyman.ru/wp-content/uploads/2020/06/Geograficheskie-ogranicheniya-po-kartam-Gazprombanka.jpg')
      bot.send_photo(message.chat.id, photo1,'🪙Кэшбэк 35% на всё самое важное\n🆓Бесплатно\nвыпуск, обслуживание, доставка\nДо 5 000 кэшбэк\nкаждый месяц\n35% кэшбэк на топовые категории\nс 1 августа 2024 по 31 января 2025\n🏷️Маркетплейсы и супермаркеты\n🏷️Кафе, рестораны и фастфуд\n🏷️Одежда и обувь\n🏷️Такси, общественный транспорт и АЗС\n🏷️ЖКХ и Госуслуги (штрафы и налоги)\nПодтвердите участие в приложении/интернет-банке в разделе «Кэшбэк баллами» до 31 января 2025. Мин. траты — 5 000 ₽ в мес.')
      text = '[Оформить сейчас](https://clck.ru/3E6XFY)'
      bot.send_message(message.chat.id, text, parse_mode='MarkdownV2')
  elif message.text == 'МТС банк':
      # Действия при нажатии на кнопку 2
      photo2 = urlopen('https://cdn.viberu.ru/help/zzqkxg0452g.jpg')
      bot.send_photo(message.chat.id, photo2, '\n💳Первая дебетовая карта со скидкой везде\n🆓Бесплатный выпуск\nСкидка до 10 000 ₽ каждый месяц\n🪙До 19% годовых на ежедневный остаток по МТС Счёту\n🛍️Скидка\n1% — на любые покупки\n3%* — на покупки в интернете первые два месяца и дальше при совершении 25 покупок за предыдущий месяц, а также для зарплатных клиентов\n*доступно только для первой карты Скидка везде с лояльностью «Скидка»\nМаксимальный размер скидки\n10 000 ₽/мес\nКешбэк бонусами с подпиской МТС Premium\n5% в супермаркетах.\n')
      #bot.reply_to(message,   )
      text2 = '[Оформить сейчас](https://clck.ru/3E9dgR)'
      bot.send_message(message.chat.id, text2, parse_mode='MarkdownV2')
  elif message.text == 'Тинькофф':
      photo3 = urlopen(
          'https://api-reforum.banki.ru/reforum/c4/10/31/7c/2d/sc5p16c43e83eea7.jpg')
      bot.send_photo(message.chat.id, photo3,
                     '🪙Повышенный кэшбэк\nДо 30% у партнеров и до 15% в выбранных категориях и местах\n🔥0 ₽ за обслуживание\n💰Кэшбэк рублями, а не бонусами\nДо 30% у партнеров, до 15% в категории «Развлечения», 10% — «Музыка», 7% — «Фастфуд» в первый месяц\n🆓Снятие без комиссии\nДо 500 000 ₽ в банкоматах Т‑Банка, от 3000 до 100 000 ₽ в других банкоматах\n')
      text3 = '[Оформить сейчас](https://clck.ru/3E9drk)'
      bot.send_message(message.chat.id, text3, parse_mode='MarkdownV2')
  else:
      # Действия при получении другого сообщения
      bot.reply_to(message, 'Повторите запрос!')

bot.polling()