#!/usr/bin/env python3 
import telegram

from telegram.ext import Updater, CommandHandler
import requests
from bs4 import BeautifulSoup

token = "5774518789:AAFto269nzsoQhpu0yq-NJAb76I_e2Ffezw"

def start(update, context):
    chat_id = update.effective_chat.id
    update.message.reply_text("start")
    print("start called from chat with id = {}".format(chat_id))


def end(update, context):
    chat_id = update.effective_chat.id
    
    update.message.reply_text("end12")
    print("end called from chat with id = {}".format(chat_id))

def menu(update, context):
    update.message.reply_text("te lo mando subito!")
    url = "https://www.dsu.toscana.it/i-menu"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
 
    links = soup.find_all('a')
  
    i = 0

    l=""
    for link in links:
	    if ('MENSA+MARTIRI' in link.get('href', [])):
	    	l=str(link)[10:134]
    headers = {
    "User-Agent": "Chrome/51.0.2704.103",
    }
    url = "https://www.dsu.toscana.it/"+l
    response = requests.get(url, headers=headers)
    update.message.reply_photo(photo=response.content)
    #context.bot.sendDocument(update.effective_chat.id,response.content)
def foto(update,context):
    update.message.reply_photo(photo='https://media-assets.wired.it/photos/615db921d8b66b13086d090c/1:1/w_590,h_590,c_limit/wired_placeholder_dummy.png')
    
def musica(update,context):
    update.message.reply_photo(photo='https://1.bp.blogspot.com/-qtv76dVe0p4/XdysykINvuI/AAAAAAAAJys/hFV0XBHfIoI-9cecjaUUdaQk_VDaS4JAgCLcBGAsYHQ/s1600/IMG_0711.jpg')
    update.message.reply_text("la la lalala la lalalal la")
def caldo(update,context):
    update.message.reply_photo(photo=open('/home/tomm/Scaricati/photo_2022-11-22_17-26-40.jpg', 'rb'))
    update.message.reply_text("prova questo metodo!")

def main():
    updater = Updater(token)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("end", end))
    updater.dispatcher.add_handler(CommandHandler("menu", menu))
    updater.dispatcher.add_handler(CommandHandler("foto", foto))
    updater.dispatcher.add_handler(CommandHandler("musica", musica))
    updater.dispatcher.add_handler(CommandHandler("caldo",caldo))
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
