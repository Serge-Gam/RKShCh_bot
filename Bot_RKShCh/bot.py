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

storage.dict_users = {'150497180': {'team': 'video', 'user_name': 'Игорь', 'admin': 'FALSE', 'emoji': '👈', 'month': '03/2018'}, '3261372': {'team': 'video', 'user_name': 'Сергей Гамалий', 'admin': 'TRUE', 'emoji': '👈', 'month': '03/2018'}, '146250723': {'team': 'sound', 'user_name': 'Алексей Титов', 'admin': 'FALSE', 'emoji': '😎', 'month': '03/2018'}, '172974394': {'team': 'video', 'user_name': 'Николай', 'admin': 'FALSE', 'emoji': '👈', 'month': '03/2018'}}
storage.video_set = {'Петр Тенетко', 'Сергей Тимошенко', 'Сергей Гамалий', 'Валентин', 'Игорь', 'Николай', 'Дима Вологдин'}
storage.sound_set = {'Алексей Косилов', 'Владимир', 'Эрик', 'Денис', 'Светлана', 'Ясин', 'Даня Лутцев', 'Алексей Титов', 'Егор', 'Эдик', 'Тамара', 'Антон', 'Дмитрий Климкин'}
storage.dict_months_links = {'05/2018': {'name': 'Май', 'link': 'https://docs.google.com/spreadsheets/d/1QRkHR3a6aqZRFLKUdFN0HkXBHNPoXEZXhFZUz3lc870/edit?usp=sharing'}, '09/2018': {'name': 'Сентябрь', 'link': 'https://docs.google.com/spreadsheets/d/1jzWTmfOr2t8XY0VfWQQ3krFIttigXED_etgIvhR57dg/edit?usp=sharing'}, '12/2018': {'name': 'Декабрь', 'link': 'https://docs.google.com/spreadsheets/d/1sAQ5b6RuPM5bauM8zfE68fTAeKzxvVtqpP7nKfwv7c0/edit#gid=0'}, '04/2018': {'name': 'Апрель', 'link': 'https://docs.google.com/spreadsheets/d/1nGrQcbBjAezNbflZHf2Pcp1suIvNtiwWUDQ6KlbBsJI/edit#gid=0'}, '02/2018': {'name': 'Февраль', 'link': 'https://docs.google.com/spreadsheets/d/1TEDtNX9IPo03toq8W2EGAuOTxu1FzbWfC6lrvz38s2M/edit#gid=0'}, '08/2018': {'name': 'Август', 'link': 'https://docs.google.com/spreadsheets/d/1Bg5KVOHnrlNHuTQ1v-PduP-NuSUgcHkBGyZbZTyvDIM/edit?usp=sharing'}, '06/2018': {'name': 'Июнь', 'link': 'https://docs.google.com/spreadsheets/d/14NyUjtj2dzLuCCTrf8fpHaiqS4EV7etysTdOu3wt7As/edit#gid=0'}, '11/2018': {'name': 'Ноябрь', 'link': 'https://docs.google.com/spreadsheets/d/1PJGRPOO5mcwESGwglhXdetcgIwthiBnRtI6VpdDu8r8/edit?usp=sharing'}, '01/2018': {'name': 'Январь', 'link': ''}, '10/2018': {'name': 'Октябрь', 'link': 'https://docs.google.com/spreadsheets/d/1PeFVKxqsuRNo2OT-D6cHZBQmFoZvbp7WCL-bqwi1KIM/edit#gid=0'}, '03/2018': {'name': 'Март', 'link': 'https://docs.google.com/spreadsheets/d/1GwxoMmKZSULq_-w8KtEEsbVdefHCxpFzZHD0trux0aU/edit#gid=0'}, '07/2018': {'name': 'Июль', 'link': 'https://docs.google.com/spreadsheets/d/1X7Hho2M29Aet19kR3n7WAM1BMBllp3e0hhpHW_d2RC0/edit?usp=sharing'}}



# загружаем данные из гугл таблицы
# storage.download_data()
# print('ВСЁ ПОЛУЧИЛОСЬ!')
# print(storage.dict_users)


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
	print(message.text)
	user_id = message.chat.id
	if authentication_passed(user_id):


		if message.text == 'Выбрать Месяц':
			response_text = 'Выберите месяц'
			bot.send_message(message.chat.id, response_text, parse_mode='Markdown', reply_markup=markups.generate_choose_month_markup())

		if message.text == 'Отмена':
			response_text = 'Отмена так отмена..'
			bot.send_message (message.chat.id, response_text, parse_mode='Markdown',
							  reply_markup=markups.generate_regular_markup())
		#меняем месяц
		if re.match('\w+\s\d{4}',message.text):
			month, year  = (message.text).split(' ')[0],(message.text).split(' ')[1]
			if month in constants.rus_months:
				month_number = str(constants.rus_months.index(month) + 1)
				if len(month_number) == 1:
					month_number = '0' + month_number
				month_code = '/'.join([month_number,year])
				storage.dict_users[str(user_id)][month] = month_code
				print('success')
				response_text = 'Месяц изменен на {}'.format(message.text)
				bot.send_message (message.chat.id, response_text, parse_mode='Markdown',
								  reply_markup=markups.generate_regular_markup())

		# else:
		# 	response_text = 'Привет {}'.format (message.from_user.first_name)
		# 	bot.send_message (message.chat.id, response_text, parse_mode='Markdown',
		# 					  reply_markup=markups.generate_regular_markup ())






	else:
		bot.send_message (message.chat.id, constants.message_user_not_found)

if __name__ == '__main__':
	bot.polling (none_stop=True)