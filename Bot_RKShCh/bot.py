import os
import re
import telebot
import storage
import parser
#import Db_lib
import constants
import markups
from telebot import types
from security import authentication_passed, user_is_admin

token = os.environ['TELEGRAM_TOKEN']

bot = telebot.TeleBot(token)

# @bot.message_handler(commands=['update_storage'])
# def storage(message):
# 	user_id = message.chat.id
# 	if authentication_passed (user_id) and user_is_admin (user_id):
# 		storage.dict_users = Db_lib.download_dict_users ()
# 		# response_text ='#stage1# dict_users downloading...'
# 		# bot.send_message (message.chat.id, response_text, parse_mode='Markdown',
# 		# 				  reply_markup=telebot.types.ReplyKeyboardRemove)
# 		# storage.dict_users = Db_lib.download_dict_users ()
# 		# response_text = '#stage1# complete'
# 		# bot.send_message (message.chat.id, response_text, parse_mode='Markdown',
# 		# 				  reply_markup=telebot.types.ReplyKeyboardRemove)
#         #
# 		# response_text = '#stage2# video_set & sound_set downloading...'
# 		# bot.send_message (message.chat.id, response_text, parse_mode='Markdown',
# 		# 				  reply_markup=telebot.types.ReplyKeyboardRemove)
# 		# storage.video_set = Db_lib.download_video_set ()
# 		# storage.sound_set = Db_lib.download_sound_set ()
# 		# response_text = '#stage2# complete'
# 		# bot.send_message (message.chat.id, response_text, parse_mode='Markdown',
# 		# 				  reply_markup=telebot.types.ReplyKeyboardRemove)
#         #
# 		# response_text = '#stage3# dict_months_links updating...'
# 		# bot.send_message (message.chat.id, response_text, parse_mode='Markdown',
# 		# 				  reply_markup=telebot.types.ReplyKeyboardRemove)
# 		# storage.dict_months_links = Db_lib.download_dict_months_links ()
#         #
# 		# response_text = '#stage3# complete\nBot is ready to play'
# 		# bot.send_message (message.chat.id, response_text, parse_mode='Markdown',
# 		# 				  reply_markup=markups.generate_regular_markup ())
#
# 	else:
# 		bot.send_message (message.chat.id, constants.message_user_not_found)

@bot.message_handler(commands=['start'])
def start(message):
	user_id = message.chat.id
	if authentication_passed(user_id):
		response_text = parser.make_rasp_for_user(user_id)
		bot.send_message(message.chat.id, response_text, parse_mode='Markdown', reply_markup=markups.generate_regular_markup())
	else:
		bot.send_message (message.chat.id, constants.message_user_not_found)

@bot.message_handler(commands=['help'])
def help(message):
	user_id = message.chat.id
	if authentication_passed(user_id) and user_is_admin(user_id):
		bot.send_message (message.chat.id, constants.message_manual_admin, parse_mode='Markdown', reply_markup=markups.generate_regular_markup())
	elif authentication_passed(user_id):
		bot.send_message (message.chat.id, constants.message_manual, parse_mode='Markdown', reply_markup=markups.generate_regular_markup())
	else:
		bot.send_message (message.chat.id, constants.message_user_not_found)

@bot.message_handler(commands=['update'])
def test(message):
	user_id = message.chat.id
	if authentication_passed(user_id):
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
	if authentication_passed(user_id):
		bot.send_message (3261372, '👁'+ str (user_id) + storage.dict_users[str(user_id)]['user_name'] + ' '+ message.text)


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
				response_text = 'Месяц изменен на {}'.format(message.text)
				bot.send_message (message.chat.id, response_text, parse_mode='Markdown',
								  reply_markup=markups.generate_regular_markup())
				response_text = parser.make_rasp_for_user (user_id)
				bot.send_message (message.chat.id, response_text, parse_mode='Markdown',
								  reply_markup=markups.generate_regular_markup ())
				#Db_lib.upload_month_code(user_id,month_code)
		#меняем эмоджи
		elif message.text[:5].lower() == 'emoji':
			emoji = message.text.split(' ')[1]
			storage.dict_users[str(user_id)]['emoji'] = emoji
			#Db_lib.upload_emoji(user_id, emoji)
			response_text = 'Сохранил ваш emoji: ' + emoji + '👌'
			bot.send_message(message.chat.id, response_text, reply_markup=markups.generate_regular_markup())



		else:
			response_text = 'Привет {}, как бы это так но не эвок'.format (message.from_user.first_name)
			bot.send_message (message.chat.id, response_text, parse_mode='Markdown',
							  reply_markup=types.ReplyKeyboardRemove())

	else:
		bot.send_message (message.chat.id, constants.message_user_not_found)
		bot.send_message (3261372,'👁' + str (user_id) + ' ' + message.text)

if __name__ == '__main__':
	bot.polling (none_stop=True)