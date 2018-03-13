from telebot import types
from storage import dict_months_links
from datetime import date
def generate_regular_markup():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard = True, resize_keyboard = True)
    markup.add('/update')
    markup.add('Выбрать Месяц')
    return markup
    #создаем массив и записываем в него все элементы

def generate_choose_month_markup():
    button_list = []
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard= True)
    markup.add('Отмена')
    for key in dict_months_links:
        year = key.split('/')[1]
        month_number = key.split('/')[0]+'_'
        year_today = date.today().year
        month_today = date.today().month
        if year_today == int(year) and month_today == int(month_number[:-1]):
            button_text = ' '.join([month_number,dict_months_links[key]['name'],str(year)+'🗓'])
        else:
            button_text = ' '.join([month_number,dict_months_links[key]['name'],str(year)])
        button_list.append(button_text)
    button_list.sort()

    button_final_list = []
    for button in button_list:
        words = button.split(' ')
        button_final = ' '.join([words[1],words[2]])
        button_final_list.append(button_final)

    for item in button_final_list:
        markup.add(item)
    markup.add('Отмена')
    return markup