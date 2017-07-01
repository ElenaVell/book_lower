import logging
import random
import book_list
import fiction_list
import love_book
import detective
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO, filename='bot.log')

def keyboard_recomend(bot,update,user_data = {}):
    mytext= '''Answer some questionsб, please: {}
               Do you like detectives? If answer -YES- press 'A' button.
               If you prefer science fiction press 'B' button.
               If you love storyes fiction press 'C' button.
               If you prefer thrillers press 'D' button.
               If you Humorous storyes fiction press 'E' button.
               If you want to finish press '=' button.
    '''.format(update.message.chat.first_name)
    logging.info('User{} press /key'.format(update.message.chat.first_name))
    custom_keyboard = [['A', 'B', 'C'],
                       ['D', 'E','=']]
    user_data['key'] = True
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)
    update.message.reply_text(mytext, reply_markup=reply_markup)


def chat(bot,update,user_data={}):
    reply_markup=None
    text=update.message.text
    logging.info("MSG: {}".format(text))
    if user_data.get('key'):
        if text == '=':
            #get_answers = user_data.get('answer', [])
            #logging.info("for answers: {}".format(get_answers))
            #del user_data['key']
            #del user_data['answer']
            reply_markup= ReplyKeyboardRemove()
            logging.info("remove keyboard")
            text="Have a nice day!: {}".format(update.message.chat.first_name)
        else:
            if text == 'A':
                #get_answers = user_data.get('answer', [])
                #user_data['answer']=get_answers
                update.message.reply_text(random.choice(detective.detective))
                logging.info("Answers: {}".format(get_answers))
            if text == 'B':
                #get_answers = user_data.get('answer', [])
                #user_data['answer']=get_answers
                update.message.reply_text(random.choice(fiction_list.fiction_list))
                logging.info("Answers: {}".format(get_answers))
            if text == 'C':
                #get_answers = user_data.get('answer', [])
                #user_data['answer']=get_answers
                update.message.reply_text(random.choice(book_list.book_list))
                logging.info("Answers: {}".format(get_answers))
            if text == 'D':
                #get_answers = user_data.get('answer', [])
                #user_data['answer']=get_answers
                update.message.reply_text(random.choice(love_book.love_book))
                logging.info("Answers: {}".format(get_answers))
            if text == 'E':
                #get_answers = user_data.get('answer', [])
                #user_data['answer']=get_answers
                update.message.reply_text(random.choice(book_list.book_list))
                logging.info("Answers: {}".format(get_answers))
        

    update.message.reply_text(text, reply_markup=reply_markup)
