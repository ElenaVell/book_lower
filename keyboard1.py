import logging
import random
import book_list
import fiction_list
import love_book
import detective
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from db_books import Book

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO, filename='bot.log')
interview =[{'Answer some questions {}, please:': ['YES', 'NO']}, {'How old are you {}?': ['0-20', '20-30', '30-40','40-50', '50-60', '<50']},
            {'Are you a man or a women {}?': ['MAN','WOMEN']}, {'What kind of book gener do you prefer?': ['Detective','Thriller', 'Love story', 'Humorous story', 'Fantasy', 'Something else']}]

def keyboard_1(bot,update,user_data = {}):
    mytext= '''Hello {}, I will recomend you some books. 
    '''.format(update.message.chat.first_name)
    logging.info('User{} press /key'.format(update.message.chat.first_name))
    update.message.reply_text(mytext)
    user_data['last_command'] = "key"

    mytext= 'Answer some questions {}, please:'.format(update.message.chat.first_name)
    logging.info('User{} answer {} question'.format(update.message.chat.first_name,1))
    custom_keyboard = [interview[0]['Answer some questions {}, please:']]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)
    update.message.reply_text(mytext, reply_markup=reply_markup)


def keyboard_2(bot,update,user_data = {}):   
    user_data['last_command'] = "key"
    mytext= 'How old are you {}?'.format(update.message.chat.first_name)
    logging.info('User{} answer {} question'.format(update.message.chat.first_name,2))
    custom_keyboard = [interview[1]['How old are you {}?']]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)
    update.message.reply_text(mytext, reply_markup=reply_markup)

def keyboard_3(bot,update,user_data = {}):   
    user_data['last_command'] = "key"
    mytext= 'Are you a man or a women {}?'.format(update.message.chat.first_name)
    logging.info('User{} answer {} question'.format(update.message.chat.first_name,3))
    custom_keyboard = [interview[2]['Are you a man or a women {}?']]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)
    update.message.reply_text(mytext, reply_markup=reply_markup)

def keyboard_4(bot,update,user_data = {}):   
    user_data['last_command'] = "key"
    mytext= 'What kind of book gener do you prefer?'.format(update.message.chat.first_name)
    logging.info('User{} answer {} question'.format(update.message.chat.first_name,4))
    custom_keyboard = [interview[3]['What kind of book gener do you prefer?']]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)
    update.message.reply_text(mytext, reply_markup=reply_markup)
    

def key_chat(bot,update,user_data={}):
    reply_markup=None
    text=update.message.text
    logging.info("MSG: {}".format(text))
    
    if text == 'NO':
        get_answers = user_data.get('answer', [])
        logging.info("for answers: {}".format(get_answers))
        #del user_data['key']
        #del user_data['answer']
        reply_markup= ReplyKeyboardRemove()
        logging.info("remove keyboard")
        text="Result: {}:".format(get_answers)
        update.message.reply_text('BAY {}!'.format(update.message.chat.first_name), reply_markup=reply_markup)
    else:
        text =  update.message.text
        if text == 'YES':
            keyboard_2(bot,update,user_data={})
            get_answers = user_data.get('answer', [])
            user_data['answer']=get_answers
            get_answers.append(text)
            logging.info("Answers: {}".format(get_answers))
        if text == '0-20'or text=='20-30' or text =='30-40' or text == '40-50' or text == '50-60' or text =='<50':
            keyboard_3(bot,update,user_data={})
            get_answers = user_data.get('answer', [])
            user_data['answer']=get_answers
            get_answers.append(text)
            logging.info("Answers: {}".format(get_answers)) 
        if text == 'WOMEN' or text =='MAN':
            keyboard_4(bot,update,user_data={})
            get_answers = user_data.get('answer', [])
            user_data['answer']=get_answers
            get_answers.append(text)
            logging.info("Answers: {}".format(get_answers))
        if text == 'Detective' or text == 'Thriller' or text ==  'Love story' or text ==  'Humorous story' or text ==  'Fantasy' or text ==  'Something else':
            get_answers = user_data.get('answer', [])
            get_answers.append(text)
            user_data['answer']=get_answers
            logging.info("Answers: {}".format(get_answers))
            get_answers = user_data.get('answer', [])
            get_answers.append(update.message.chat.id)
            logging.info("for answers: {}".format(get_answers))
            reply_markup= ReplyKeyboardRemove()
            logging.info("remove keyboard")
            text="Result: {}:".format(get_answers)
            #results=dict(zip(['Age','Gender','Genre_prefer'], get_answers[1:]))
            #results['user_id'] = update.message.chat.id
            books_from_db = Book
            b=[]
            if 'Detective' in get_answers:
                books = books_from_db.query.filter(Book.genre == 'Детективы').all()
                for book in books:
                    b.append(str(book))
                update.message.reply_text(random.choice(b), reply_markup=reply_markup)
                del user_data['last_command']
                del user_data['answer']
            elif 'Thriller' in get_answers:
                books = books_from_db.query.filter(Book.genre == 'Ужасы.Мистика.Триллер').all()
                for book in books:
                    b.append(str(book))
                update.message.reply_text(random.choice(b), reply_markup=reply_markup)
                del user_data['last_command']
                del user_data['answer']
            elif 'Love story' in get_answers:
                books = books_from_db.query.filter(Book.genre == 'Любовные романы').all()
                for book in books:
                    b.append(str(book))
                update.message.reply_text(random.choice(b), reply_markup=reply_markup)
                del user_data['last_command']
                del user_data['answer']
            elif 'Humorous story' in get_answers:
                books = books_from_db.query.filter(Book.genre == 'Юмористическая литература').all()
                for book in books:
                    b.append(str(book))
                update.message.reply_text(random.choice(b), reply_markup=reply_markup)
                del user_data['last_command']
                del user_data['answer']
            elif 'Fantasy' in get_answers:
                books = books_from_db.query.filter(Book.genre == 'Фантастика.Фентези').all()
                for book in books:
                    b.append(str(book))
                update.message.reply_text(random.choice(b), reply_markup=reply_markup)
                del user_data['last_command']
                del user_data['answer']
            else:
                books = books_from_db.query.filter(Book.genre == 'Бизнес-Книги').all()
                for book in books:
                    b.append(str(book))
                update.message.reply_text(random.choice(b), reply_markup=reply_markup)
                del user_data['last_command']
                del user_data['answer']




    #update.message.reply_text(text, reply_markup=reply_markup)
    #update.message.reply_text(results, reply_markup=reply_markup)
