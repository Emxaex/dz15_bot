import telebot
import database

menu1 = telebot.types.InlineKeyboardMarkup()
menu1.row(
    telebot.types.InlineKeyboardButton('Проживающие', callback_data='help'),
    telebot.types.InlineKeyboardButton('Зарегистрироваться', callback_data='register')
    )

bot=telebot.TeleBot('7652378304:AAEMNt7Fk36IbNfzRiOQ7bpGbzFDAbziAmc')
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, f'Добро пожаловать \n'
                                           f'Выберите что хотите сделать', reply_markup=menu1 )

#В общем это оброботчик когда человек нажмёт на inline кнопку. call это просто имя переменной
#которое может быть любое. Но у программистов принято называть call
#можно задать ещё условие по типу
#@bot.callback_query_handler(func=lambda call: call.data == 'register')
#этот обработчик следит чтобы именно на register нажали, а help он будет игнорировать
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data=='help':
        info = database.show_info()
        for name, tel, hotel in info:
            message = f'Имя: {name}\nТелефонный номер: {tel}\nНомер комнаты: {hotel}'
            bot.send_message(call.message.chat.id,message)
      #  bot.register_next_step_handler(call.message,help_info)
    elif call.data=='register':
        bot.send_message(call.message.chat.id, 'Введите ваше имя, номер телефона и номер желаемой комнаты через пробел')
        bot.register_next_step_handler(call.message,register)


def register(message):
    print(message)
    user_info = message.text.strip()
    #берёт значение из user_info и разделяет его
    user_name,user_number,hotel_number = [x.strip() for x in user_info.split(' ')]
    database.add_client(user_name,user_number,hotel_number)
    bot.send_message(message.from_user.id, "Ты успешно зарегистрирован! Спасибо!")



bot.polling(non_stop=True)
