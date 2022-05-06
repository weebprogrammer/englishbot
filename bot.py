import telebot
import requests
import json 


from config import BOTTOKEN, DISKTOKEN
from files import files


bot = telebot.TeleBot(BOTTOKEN)


def diskdownload(message: str):
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {DISKTOKEN}'}
    URL = 'https://cloud-api.yandex.net/v1/disk/resources'
    fileresponse = requests.get(URL+f'?path=%2Fenglishfile%2F{message}.mp3', headers=headers).content
    aboutfilejson = json.loads(fileresponse)
    file = requests.get(aboutfilejson['file'], headers=headers).content
    return file


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

    if message.text+'.mp3' in files:
        file = diskdownload(message.text)
        bot.send_audio(message.chat.id, audio=file, title=f'{message.text}.mp3')
    else:
        bot.reply_to(message, 'something went wrong! Check the number and try again.')


if __name__ == '__main__':
    bot.polling(none_stop=True)
