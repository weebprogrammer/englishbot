import os
import telebot
import yadisk


from utils import BOTTOKEN, DISKTOKEN


bot = telebot.TeleBot(BOTTOKEN)
disk = yadisk.YaDisk(DISKTOKEN)



def csvlogger(column1: str, column2: str, column3: str):
    columns = [column1, column2, column3]
    with open('log.csv', 'a', encoding='utf-8') as f:
        f.write(','.join(columns)+'\n')


@bot.message_handler(commands=['start', 'help'])
def echo(message):
    bot.reply_to(message, "Hi! I'm English File Elementary 4e audio bot. Send me the number of audio you need!")


@bot.message_handler(content_types=['text', ])
def main(message):
    csvlogger(str(message.chat.id), message.from_user.first_name, message.text)
    


if __name__ == '__main__':
    bot.polling()
