import re
import telebot
import parser
import storage
import Db_lib
import constants
import markups
from telebot import types
from security import authentication_passed

token = '524774362:AAFwD39cVza7vDvycI0sJjHA0ebVCTW2Aeo'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['update'])
def test(message):
	print(storage.dict_users)
	user_id = message.chat.id
	if authentication_passed(user_id):
		print('authentication_passed')
		print(type(user_id))
		response_text = parser.make_rasp_for_user(user_id)
		bot.send_message(message.chat.id, response_text, parse_mode='Markdown', reply_markup=markups.generate_regular_markup())
	else:
		bot.send_message (message.chat.id, constants.message_user_not_found)

@bot.message_handler(commands=['01','02','03','04','05','06','07','08','09','10','11','12',
							   '13','14','15','16','17','18','19','20','21','22','23','24',
							   '25','26','27','28','29','30','31'])
def get_schadule_for_the_day(message):
	user_id = message.chat.id
	day = message.text
	if authentication_passed(user_id) == True:
		response_text = parser.make_rasp_for_date(user_id, day)
		bot.send_message(message.chat.id, response_text, parse_mode='Markdown', reply_markup=markups.generate_regular_markup())
	else:
		bot.send_message (message.chat.id, constants.message_user_not_found , parse_mode='Markdown', reply_markup=markups.generate_regular_markup())





@bot.message_handler(content_types=['text'])
def text_handler(message):
	user_id = message.chat.id
	bot.send_message (3261372, '👁'+ str (user_id) + ' '+ message.text)
	if authentication_passed(user_id):


		if message.text == 'Выбрать Месяц':
			response_text = 'Выберите месяц'
			bot.send_message(message.chat.id, response_text, parse_mode='Markdown', reply_markup=markups.generate_choose_month_markup())

		elif message.text == 'Отмена':
			response_text = 'Отмена так отмена..🤷‍♀️'
			bot.send_message (message.chat.id, response_text, parse_mode='Markdown',
							  reply_markup=markups.generate_regular_markup())

		#меняем месяц
		elif re.match('\w+\s\d{4}',message.text):
			month, year  = (message.text).split(' ')[0],(message.text).split(' ')[1]
			if month in constants.rus_months:
				month_number = str(constants.rus_months.index(month) + 1)
				if len(month_number) == 1:
					month_number = '0' + month_number
				month_code = '/'.join([month_number,year])
				storage.dict_users[str(user_id)]['month'] = month_code
				print('success')
				print(storage.dict_users[str(user_id)])
				response_text = 'Месяц изменен на {}'.format(message.text)
				bot.send_message (message.chat.id, response_text, parse_mode='Markdown',
								  reply_markup=markups.generate_regular_markup())
				response_text = parser.make_rasp_for_user (user_id)
				bot.send_message (message.chat.id, response_text, parse_mode='Markdown',
								  reply_markup=markups.generate_regular_markup ())

		else:
			response_text = 'Привет {}, как бы это так но не эвок'.format (message.from_user.first_name)
			bot.send_message (message.chat.id, response_text, parse_mode='Markdown',
							  reply_markup=types.ReplyKeyboardRemove())






	else:
		bot.send_message (message.chat.id, constants.message_user_not_found)

if __name__ == '__main__':
	bot.polling (none_stop=True)