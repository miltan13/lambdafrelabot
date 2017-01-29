# -*- config: utf-9 -*-

import config
import telebot

from datetime import datetime, date, time

nowday = config.wd[datetime.now().strftime("%A, %d. %B %Y %I:%M%p").split()[0][0:-1]]

print(nowday)

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def handle_start(message):
	bot.send_message(message.chat.id, config.start)
	print(message.chat.id)

@bot.message_handler(commands=['help'])
def handle_help(message):
	markup = telebot.types.ReplyKeyboardMarkup()
	markup.row('Репозиторий лямбды на гите', 'Номер телефона Хайзенберга')
	markup.row()
	bot.send_message(message.chat.id, 'Что ты хочешь узнать?', reply_markup=markup)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
	if 'омер' in message.text and ('айзенберг' in message.text or 'имур' in message.text):
		bot.send_message(message.chat.id, '+7(916)126-55-01 \n Звонить, если что-то не работает!')
	
	elif 'епозиторий лямбды' in message.text :
		bot.send_message(message.chat.id, 'https://github.com/lambdafrela/')
	
	elif message.text in config.ban: 
		bot.send_message(message.chat.id, 'Ты плохой, не ругайся :(')
	
	elif 'О боте' in message.text or 'о боте' in message.text:
		bot.send.message(message.chat.id, 'Бота написал Сорокин Сергей с ФРЭЛА на языке Python3. Потому что могу.')
	
	elif 'М4О-111Б' in message.text and message.chat.id == 64634999:		
		markup = telebot.types.ReplyKeyboardMarkup()
		markup.row('Расписание на сегодня', 'Расписание на завтра')
		markup.row('Когда лаба?', 'Какая пара следующая?')
		bot.send_message(message.chat.id, 'Дарова, Сергуня!', reply_markup=markup)
	
	else: 
		bot.send_message(message.chat.id, 'Я не сделал дофига крутого бота для общения. Лучше запусти /help или /start чтобы узнать больше')


if __name__ == '__main__':
	bot.polling(none_stop=True)
