from telebot import types

def generate_regular_markup():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True)
    markup.add('Январь2018')
    #создаем массив и записываем в него все элементы
    return markup