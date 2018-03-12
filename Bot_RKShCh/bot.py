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


# загружаем данные из гугл таблицы
# storage.download_data()
# print('ВСЁ ПОЛУЧИЛОСЬ!')

@bot.message_handler(commands=['update'])
def test(message):
	user_id = str(message.chat.id)
	if authentication_passed(user_id):
		response_text = parser.make_rasp_for_user(user_id)

		bot.send_message(message.chat.id, response_text, parse_mode='Markdown')
	else:
		bot.send_message (message.chat.id, constants.message_user_not_found)


@bot.message_handler(commands=['01','02','03','04','05','06','07','08','09','10','11','12',
							   '13','14','15','16','17','18','19','20','21','22','23','24',
							   '25','26','27','28','29','30','31'])

def get_me_a_schadule_for_the_day(message):
	markup = markups.generate_regular_markup()
	user_id = str(message.chat.id)
	day = message.text
	if authentication_passed(user_id) == True:
		response_text = parser.make_rasp_for_date(user_id, day)
		bot.send_message(message.chat.id, response_text, parse_mode='Markdown')
	else:
		bot.send_message (message.chat.id, constants.message_user_not_found , parse_mode='Markdown', reply_markup= markup)

if __name__ == '__main__':
	bot.polling (none_stop=True)