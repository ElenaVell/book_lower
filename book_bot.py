import logging
import settings
import random
import book_list
import fiction_list
import love_book
import detective
from keyboard1 import keyboard_1, keyboard_2, keyboard_3, keyboard_4, chat
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler

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



def random_recomend(bot,update,args=None):
    if args is None:
        args = []
    if args!=[]:
        update.message.reply_text(random.choice(book_list.book_list))

    else:
        update.message.reply_text('No words input')


def main():
    updtr = Updater(settings.TELEGRAM_API_KEY)

    updtr.dispatcher.add_handler(CommandHandler('start',start_bot))
    updtr.dispatcher.add_handler(CommandHandler('go', random_recomend, pass_args=True))
    updtr.dispatcher.add_handler(CommandHandler('key', keyboard_1, pass_user_data=True))
    updtr.dispatcher.add_handler(MessageHandler(Filters.text, chat, pass_user_data=True))

    updtr.start_polling()
    updtr.idle()

if __name__=='__main__':
    logging.info('Bot started')
    main()