import telebot
import parser
import storage
from telebot import types

token = '524774362:AAFwD39cVza7vDvycI0sJjHA0ebVCTW2Aeo'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['test'])
def keybr(message):
	user_id = str(message.chat.id)
	if user_id in storage.dict_users:
		#response_text = parser.get_rasp_for_user(user_id)
		response_text = parser.get_rasp_for_date(user_id, '/02')
		bot.send_message(message.chat.id, response_text, parse_mode='Markdown')
	else:
		print('Error')

@bot.message_handler(commands=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31'])
def

if __name__ == '__main__':
	bot.polling(none_stop=True)




