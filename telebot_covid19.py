import requests, json, telebot
import telebot
from jsontraverse.parser import JsonTraverseParser
from datetime import datetime

url = requests.get('https://api.kawalcorona.com/indonesia')

url_global_positif = requests.get('https://api.kawalcorona.com/positif')

url_global_sembuh = requests.get('https://api.kawalcorona.com/sembuh')

url_global_meninggal = requests.get('https://api.kawalcorona.com/meninggal')

data = url.json()
data1 = url_global_positif.json()
data2 = url_global_sembuh.json()
data3 = url_global_meninggal.json()

json_string = json.dumps(data)
json_string1 = json.dumps(data1)
json_string2 = json.dumps(data2)
json_string3 = json.dumps(data3)
#print(json_string)

parser = JsonTraverseParser(json_string)
parser1 = JsonTraverseParser(json_string1)
parser2 = JsonTraverseParser(json_string2)
parser3 = JsonTraverseParser(json_string3)
#print(parser3)

covid19_sembuh = parser.traverse("sembuh")
#print(covid19_sembuh)

covid19_positif = parser.traverse("positif")
#print(covid19_positif)

covid19_meninggal = parser.traverse("meninggal")
#print(covid19_meninggal)

covid19_dirawat = parser.traverse("dirawat")
#print(covid19_dirawat)

global_positif = parser1.traverse("value")
print(global_positif)
global_sembuh = parser2.traverse("value")
print(global_sembuh)
global_meninggal = parser3.traverse("value")
print(global_meninggal)

now = datetime.now()

with open('config.json') as f:
   token = json.load(f)

bot = telebot.TeleBot(token['telegramToken'])

@bot.message_handler(commands=['start'])
def welcome(message):
    # membalas pesan
    bot.reply_to(message, '''Bot Update Data COVID19 Indonesia
Command List :
1) /covid19

Powered By Abdul Rozaqi.''')

@bot.message_handler(regexp='covid19')
def covid19(message):
    display="Statistic COVID19 Global By kawalcorona.com\nLast Update : " +  now.strftime('%Y-%m-%d %H:%M:%S') + "\nPositif " + global_positif + "\nSembuh " + global_sembuh + "\nMeninggal " + global_meninggal +  "\n\nStatistic COVID19 Indonesia" + '\nPositif ' + covid19_positif + '\nSembuh ' + covid19_sembuh + '\nMeninggal ' + covid19_meninggal + '\nDirawat ' + covid19_dirawat
    bot.reply_to(message, display)

print("Bot Telegram sedang running")
bot.polling()

#print("""Statistic COVID19 Indoensia By kawalcorona.com
#Last Update : """, now.strftime("%Y-%m-%d %H:%M:%S") + """
#Positif""", covid19_positif, """
#Sembuh""", covid19_sembuh + """
#Meninggal""", covid19_meninggal + """
#Dirawat""", covid19_dirawat)

