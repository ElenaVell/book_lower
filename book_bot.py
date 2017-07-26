import logging
import settings
import random
import book_list
import fiction_list
import love_book
import detective
from reader import *
from keyboard1 import *
from get_recomend import*
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
import urllib
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO, filename='bot.log'
                    )

def start_bot(bot,update):
    mytext= '''Hi {}!
    I am a bot and understand {} command
    You can tell me, what was the last book, you like, and I will recomend you the next one.
    Use {} command and the title of book to start.
    '''.format(update.message.chat.first_name, '/start', '/key')
    logging.info('User{} press /start'.format(update.message.chat.first_name))
    user_id = update.message.chat.id
    update.message.reply_text(mytext)

def chat(bot,update,user_data={}):
    last_command = user_data.get('last_command')
    if last_command == "key":
        key_chat(bot,update,user_data = {})
    elif last_command == "reader":
        reader_chat(bot,update,user_data = {})
    elif last_command == "review":
        review_chat(bot,update,user_data = {})
        if review_chat(bot,update,user_data = {}) == None:
            #get_recomend_by_author(bot,update, user_data = {})
            get_recomend_by_author_chat(bot,update, user_data = {})
    else:
        update.message.reply_text("не задана команда")


def main():
    updtr = Updater(settings.TELEGRAM_API_KEY)

    updtr.dispatcher.add_handler(CommandHandler('start',start_bot))
    updtr.dispatcher.add_handler(CommandHandler('reader', reader, pass_user_data=True))
    updtr.dispatcher.add_handler(CommandHandler('key', keyboard_1, pass_user_data=True))
    updtr.dispatcher.add_handler(CommandHandler('review', get_recomend, pass_user_data=True))
    updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat, pass_user_data=True))


    updtr.start_polling()
    updtr.idle()

if __name__=='__main__':
    logging.info('Bot started')
    main()