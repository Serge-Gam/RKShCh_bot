import telebot
import parser
import storage
from telebot import types
import constants
token = '524774362:AAFwD39cVza7vDvycI0sJjHA0ebVCTW2Aeo'
bot = telebot.TeleBot(token)

#@bot.message_handler(content_types=['text'])
# def default_text(message):
#     keyboard = types.InlineKeyboardMarkup()
#     url_button = types.InlineKeyboardButton(text='Тут живет расписание на февраль',
#                                             url='https://docs.google.com/spreadsheets/d/1TEDtNX9IPo03toq8W2EGAuOTxu1FzbWfC6lrvz38s2M/edit#gid=0')
#
#     keyboard.add(url_button)
#     bot.send_message(message.chat.id, 'Тут будет расписание:', reply_markup=keyboard)


# Обычный режим


@bot.message_handler(commands=['test'])
def keybr(message):
	user_id = str(message.chat.id)
	if user_id in storage.dict_users:
		#response_text = parser.get_rasp_for_user(user_id)
		response_text = parser.get_rasp_for_date(user_id, '/02')
		bot.send_message(message.chat.id, response_text, parse_mode='Markdown')
	else:
		print('Error')


#





if __name__ == '__main__':
    bot.polling(none_stop=True)




