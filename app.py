import telebot
import config
import csv
from datetime import datetime as dt
from datetime import timedelta as td
import time
import colorama
import conDB as db
from colorama import Fore, Back, Style

colorama.init()
bot = telebot.TeleBot(config.TOKEN)

bnames = []
bdate = []
chatid = config.CHATID # chat id from config 

def send_message(message):
    bot.send_message(chatid, message)

def checkBdays():
    print('Checking bdays...')
    date = ""
    preWeek = ""
    today = dt.today().date()
    nextWeek = today + td(days=7)
    for index, item in enumerate(bdate):
        if (db.checkmessage(str(bnames[index]), str(today))):
            print(Fore.YELLOW + 'Oooops, repeated request. ' + str(bnames[index]))
            continue
        date = item
        date = dt.strptime(date, '%d-%m-%Y')
        preWeek = date - td(days=7)
        date = date.strftime('%Y-%m-%d')
        if (str(today) == str(date)):
            print(Fore.GREEN + 'Send birthday...')
            send_message('Достойный повод\nПоднять бокалы выше\nЗа наше солнце!\n'+ bnames[index] + ', с Днем Рождения!')
        if (str(nextWeek) == str(date)):
            print(Fore.GREEN + 'Send birthday week...')
            send_message('Постой-ка, ' + bnames[index] + ', у тебя же ДР через неделю!')
        db.addrow(bnames[index], today)

ContentFromCSV = []
with open('input.csv', encoding='utf8', newline='') as File:
    reader = csv.reader(File)
    for row in reader:
        ContentFromCSV += row

for s in ContentFromCSV:
    lst = s.split(';')
    year = dt.today().strftime('%Y')
    bnames.append(lst[0])
    bdate.append((lst[1] + '-' + lst[2] + '-' + year))

while True:
    res = db.checkday(str(dt.today().strftime('%Y-%m-%d')))
    print('\n')
    daynow = dt.today().strftime('%H:%M %d-%m-%Y')
    print(daynow)
    if(not res):
        db.deletedata()
    checkBdays()
    print(Style.RESET_ALL)
    print('Waiting...')
    time.sleep(86400) # 1 day in seconds



