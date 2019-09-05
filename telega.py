import telebot
import random
from telebot import types

# Tokenfffffffffffffffffffffffffffffffffffffffffffffffffffffff
bot = telebot.TeleBot("968922643:AAGok0uackE1aDV2c6-dYK76mtWTrAGMjIk")
a = ["Подтверждаю", "Да", "Угу", "Конечно", "Ага"]
b = ["Hmm", "Интересно", "Что?", "Что ещё раз?", "Ого", "Omg"]
с = ["Не", "Не подтверждаю", "Не-а", "Нууу... нет", "К сожалениею, нет"]
image = "https://www.canva.com/learn/wp-content/uploads/2018/11/best-free-stock-photos.jpg"
f = ["Муж жене \n Сегодня будем заниматься сексом по-пчелиному. \n Это как? Наверное, ты намажешь меня мёдом и будешь всю облизывать? \n Нет. Прилетела, пососала и – улетела"]
g = ["В магазине мужчина робко обращается к женщине:\n"
"– Простите, вы не подскажете, в какой отдел этого магазина\n"
"вы бы пошли, если бы у вас была тысяча рублей?\n"
"– В косметический.\n"
"– О, спасибо большое! Побежал искать жену!\n", "– Боря,и как ты смог затащить её в постель?!\n"
"– Та это всё романтика… Мы таки смотрели на звезды, я ей прочел Пушкина – и она растаяла… Не, ну и водка конечно..\n", "– Вась, джинсы твои новые я соседу отдала.\n"
"– Это в честь чего?!\n"
"– Они всё равно тебе не нравились.\n"
"– Давай, Люся, тогда маму твою соседу отдадим.\n", "В Интернете резко упало число комментариев от ведущих политологов, экономистов и экспертов – школота ушла учиться!"]


# Start, joke
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Доступные команды: \n'
                                      'Расписание - Расписание (картинкой) \n'
                                      'Понедельник - Расписание на понедельник \n'
                                      'Вторник - Расписание на вторник \n'
                                      'Среда - Расписание на среду \n'
                                      'Четверг - Расписание на четверг\n'
                                      'Пятница - Расписание на пятницу \n'
                                      'Анектод \n')




# Понедельник
@bot.message_handler(regexp="пн")
def answer(message):
    bot.send_message(message.from_user.id, '1) Обществознание \n'
    '2) Обществознание \n'
    '3) История \n'
    '4) Литература \n'
    '5) Литература \n'
    '6) Химия \n'
    '7) Анлийский \n'
    '8) Английский \n')

@bot.message_handler(regexp="Понедельник")
def answer(message):
    bot.send_message(message.from_user.id, '1) Обществознание \n'
    '2) Обществознание \n'
    '3) История \n'
    '4) Литература \n'
    '5) Литература \n'
    '6) Химия \n'
    '7) Анлийский \n'
    '8) Английский \n')

@bot.message_handler(regexp="понедельник")
def answer(message):
    bot.send_message(message.from_user.id, '1) Обществознание \n'
    '2) Обществознание \n'
    '3) История \n'
    '4) Литература \n'
    '5) Литература \n'
    '6) Химия \n'
    '7) Анлийский \n'
    '8) Английский \n')

@bot.message_handler(regexp="пон")
def answer(message):
    bot.send_message(message.from_user.id, '1) Обществознание \n'
    '2) Обществознание \n'
    '3) История \n'
    '4) Литература \n'
    '5) Литература \n'
    '6) Химия \n'
    '7) Анлийский \n'
    '8) Английский \n')

@bot.message_handler(regexp="Пон")
def answer(message):
    bot.send_message(message.from_user.id, '1) Обществознание \n'
    '2) Обществознание \n'
    '3) История \n'
    '4) Литература \n'
    '5) Литература \n'
    '6) Химия \n'
    '7) Анлийский \n'
    '8) Английский \n')

# Вторник
@bot.message_handler(regexp="вт")
def answer(message):
    bot.send_message(message.from_user.id, '1) Физика \n'
    '2) Математика \n'
    '3) Физкультура \n'
    '4) Физкультура \n'
    '5) История \n'
    '6) Обж \n'
    '7) Астронимия \n'
    '8) Физика \n')

@bot.message_handler(regexp="Вторник")
def answer(message):
    bot.send_message(message.from_user.id, '1) Физика \n'
    '2) Математика \n'
    '3) Физкультура \n'
    '4) Физкультура \n'
    '5) История \n'
    '6) Обж \n'
    '7) Астронимия \n'
    '8) Физика \n')

@bot.message_handler(regexp="Вт")
def answer(message):
    bot.send_message(message.from_user.id, '1) Физика \n'
    '2) Математика \n'
    '3) Физкультура \n'
    '4) Физкультура \n'
    '5) История \n'
    '6) Обж \n'
    '7) Астронимия \n'
    '8) Физика \n')



# Среда
@bot.message_handler(regexp="ср")
def answer(message):
    bot.send_message(message.from_user.id, '1) Английский \n'
    '2) Английский \n'
    '3) ОиТРТ \n'
    '4) РТНТ \n'
    '5) Математика \n'
    '6) Математика \n'
    '7) РТПТ \n'
    '8) РТПТ \n')

@bot.message_handler(regexp="Среда")
def answer(message):
    bot.send_message(message.from_user.id, '1) Английский \n'
    '2) Английский \n'
    '3) ОиТРТ \n'
    '4) РТНТ \n'
    '5) Математика \n'
    '6) Математика \n'
    '7) РТПТ \n'
    '8) РТПТ \n')


@bot.message_handler(regexp="Ср")
def answer(message):
    bot.send_message(message.from_user.id, '1) Английский \n'
    '2) Английский \n'
    '3) ОиТРТ \n'
    '4) РТНТ \n'
    '5) Математика \n'
    '6) Математика \n'
    '7) РТПТ \n'
    '8) РТПТ \n')

@bot.message_handler(regexp="сред")
def answer(message):
    bot.send_message(message.from_user.id, '1) Английский \n'
    '2) Английский \n'
    '3) ОиТРТ \n'
    '4) РТНТ \n'
    '5) Математика \n'
    '6) Математика \n'
    '7) РТПТ \n'
    '8) РТПТ \n')

@bot.message_handler(regexp="Сред")
def answer(message):
    bot.send_message(message.from_user.id, '1) Английский \n'
    '2) Английский \n'
    '3) ОиТРТ \n'
    '4) РТНТ \n'
    '5) Математика \n'
    '6) Математика \n'
    '7) РТПТ \n'
    '8) РТПТ \n')



# Четверг
@bot.message_handler(regexp="чт")
def answer(message):
    bot.send_message(message.from_user.id, '1) Русский \n'
    '2) Физика \n'
    '3) Математика \n'
    '4) Физкультура \n'
    '5) География \n'
    '6) Литература \n'
    '7) Биология \n')

@bot.message_handler(regexp="Четверг")
def answer(message):
    bot.send_message(message.from_user.id, '1) Русский \n'
    '2) Физика \n'
    '3) Математика \n'
    '4) Физкультура \n'
    '5) География \n'
    '6) Литература \n'
    '7) Биология \n')

@bot.message_handler(regexp="Чт")
def answer(message):
    bot.send_message(message.from_user.id, '1) Русский \n'
    '2) Физика \n'
    '3) Математика \n'
    '4) Физкультура \n'
    '5) География \n'
    '6) Литература \n'
    '7) Биология \n')

@bot.message_handler(regexp="четверг")
def answer(message):
    bot.send_message(message.from_user.id, '1) Русский \n'
    '2) Физика \n'
    '3) Математика \n'
    '4) Физкультура \n'
    '5) География \n'
    '6) Литература \n'
    '7) Биология \n')




# Пятница
@bot.message_handler(regexp="пт")
def answer(message):
    bot.send_message(message.from_user.id, '*Практика* \n'
    '*Практика* \n'
    '*Практика* \n'
    '*Практика* \n'
    '*Практика* \n'
    '*Практика*  \n'
    '*Практика* \n')

@bot.message_handler(regexp="Пятница")
def answer(message):
    bot.send_message(message.from_user.id, '*Практика* \n'
    '*Практика* \n'
    '*Практика* \n'
    '*Практика* \n'
    '*Практика* \n'
    '*Практика*  \n'
    '*Практика* \n')

@bot.message_handler(regexp="Пятн")
def answer(message):
    bot.send_message(message.from_user.id, '*Практика* \n'
    '*Практика* \n'
    '*Практика* \n'
    '*Практика* \n'
    '*Практика* \n'
    '*Практика*  \n'
    '*Практика* \n')

@bot.message_handler(regexp="Пт")
def answer(message):
    bot.send_message(message.from_user.id, '*Практика* \n'
    '*Практика* \n'
    '*Практика* \n'
    '*Практика* \n'
    '*Практика* \n'
    '*Практика*  \n'
    '*Практика* \n')

@bot.message_handler(regexp="пятн")
def answer(message):
    bot.send_message(message.from_user.id, '*Практика* \n'
    '*Практика* \n'
    '*Практика* \n'
    '*Практика* \n'
    '*Практика* \n'
    '*Практика*  \n'
    '*Практика* \n')



# Расписание
@bot.message_handler(regexp="расписание")
def answer(message):
    bot.send_photo(message.chat.id, 'https://sun9-32.userapi.com/c855536/v855536960/daf18/ivwvYRAk29o.jpg')

# Анектод
@bot.message_handler(regexp= 'Пчела')
def answer(message):
    bot.send_message(message.chat.id, f)

@bot.message_handler(regexp= 'Анектод')
def answer(message):
    bot.send_message(message.chat.id, random.choice(g))



# Reply
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, random.choice(b))




bot.polling(none_stop=True, interval=0)
