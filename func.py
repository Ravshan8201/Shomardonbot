import telegram

from cons import *
from cons import dct
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from time import sleep
from sql_cons import *
import sqlite3
def start(update, context):
    user_id = update.message.chat_id
    f_name =update.message.from_user.first_name

    context.bot.send_message(chat_id= user_id, text='{}, 👋🙃'.format(f_name))
    sleep(1)
    connect = sqlite3.connect('user_list.sqlite')
    cur = connect.cursor()
    TG_ID = cur.execute(get_id.format(user_id)).fetchall()
    stage_update = cur.execute(stage.format(user_id)).fetchall()
    try:
        TG_ID = TG_ID[0][0]
        if TG_ID== 95753147:
            id = 957531477
            context.bot.send_message(chat_id=id, text='Админ меню йукланмокда....')
            sleep(3)
            context.bot.send_message(chat_id=id, text='')
            sleep(1)
            context.bot.send_message(chat_id=id, text='Удачи')
            sleep(1)
    except Exception:
        pass
    if TG_ID == user_id:
        lang_ = cur.execute(lang_select.format(user_id)).fetchall()
        lang_=lang_[0][0]
        cur.execute(stagee.format('{}', user_id).format(2))
        k_but = [KeyboardButton(text=dct[lang_][0])]
        context.bot.send_message(chat_id=user_id, text=dct[lang_][1],
                                 reply_markup=ReplyKeyboardMarkup([k_but], resize_keyboard=True))


    if user_id != TG_ID:
        cur.execute(first_insert.format(user_id,1))
        connect.commit()
        sleep(1)
        knopka_lang = [
            InlineKeyboardButton(text='Русский язык🇷🇺', callback_data='ru')
        ]
        knopka_lang1 = [
            InlineKeyboardButton(text='''O'zbek tili🇺🇿''', callback_data='uz')
        ]
        context.bot.send_message(chat_id=user_id, text='Выберите язык:\nTilni taglang:',
                              reply_markup=InlineKeyboardMarkup([knopka_lang,knopka_lang1]))
        sleep(1)

def next_func(update, context):
    connect = sqlite3.connect('user_list.sqlite')
    cur = connect.cursor()
    user_id = update.message.chat_id
    f_name = update.message.from_user.first_name
    num = update.message.contact.phone_number
    stage_ = cur.execute(stage.format(user_id)).fetchall()
    lang_= cur.execute(lang_select.format(user_id)).fetchall()
    connect.commit()
    message = update.message.text
    message = str(message)
    try:
       stage_ = stage_[0][0]
       lang_ = lang_[0][0]
       if message.lower() == 'davom etish>>>' or  message ==dct[lang_][0] or stage_ == 2 or message.lower() == 'далее>>>' or stage_ == 2  :
           cur.execute(stagee.format('{}', user_id).format(3))
           connect.commit()
           but =  [KeyboardButton(text=keydct[lang_][0]),
                   KeyboardButton(text=keydct[lang_][1])]
           but2 = [KeyboardButton(text=keydct[lang_][2]),
                   KeyboardButton(text=keydct[lang_][3])]
           context.bot.send_message(chat_id=user_id, text=dct[lang_][0] , reply_markup=ReplyKeyboardMarkup([but,but2], resize_keyboard=True))
       message = update.message.text
       message = str(message)
       stage_2 = cur.execute(stage.format(user_id)).fetchall()
       stage_2 = stage_2[0][0]



       if message == '🚀Интернет-пакеты' and stage_2 == 3 or  message=='🚀Internet-paketlar'  and stage_2 == 3:
             cur.execute(stagee.format('{}', user_id).format(3.1))
             connect.commit()
             but = [KeyboardButton(text='🐝Beeline'),
                    KeyboardButton(text='💎Uzmobile')]
             b3 =  [KeyboardButton(text='🔻Mobiuz'),
                    KeyboardButton(text='🟪Ucell')]
             b5 =  [KeyboardButton(text='👨‍👩‍👧‍👦Humans'),
                    KeyboardButton(text=dct[lang_][0])]
             context.bot.send_message(chat_id=user_id, text=dct[lang_][2],
                                     reply_markup=ReplyKeyboardMarkup([but, b3, b5], resize_keyboard=True))
       #  TUUUGATILMAGAN MB OLISH
       stage_2 = cur.execute(stage.format(user_id)).fetchall()
       stage_2 = stage_2[0][0]
       if message == '🐝Beeline' and stage_2 == 3.1:
           pass
       if message == '💎Uzmobile'and stage_2 == 3.1:
           pass
       if message == '🔻Mobiuz'and stage_2 == 3.1:
           pass
       if message == '🟪Ucell'and stage_2 == 3.1:
           pass
       if message == '👨‍👩‍👧‍👦Humans'and stage_2 == 3.1:
           pass


       if message == '🎁Красивые номера' and stage_2 == 3 or  message=='🎁Yangi chiroyli nomerlar'  and stage_2 == 3:
             cur.execute(stagee.format('{}', user_id).format(3.2))
             connect.commit()
             but = [KeyboardButton(text='Beeline'),
                    KeyboardButton(text='Uzmobile')]
             b3 =  [KeyboardButton(text='Mobiuz'),
                    KeyboardButton(text='Ucell')]
             b5 =  [KeyboardButton(text='Humans'),
                    KeyboardButton(text=dct[lang_][0])]
             context.bot.send_message(chat_id=user_id, text=dct[lang_][2],
                                     reply_markup=ReplyKeyboardMarkup([but, b3, b5], resize_keyboard=True))
       # TUGATILMAGAN!!!!!!!!! NOMERLAAAAAR
       stage_2 = cur.execute(stage.format(user_id)).fetchall()
       stage_2 = stage_2[0][0]
       if message == 'Beeline'and stage_2 == 3.2:
           pass
       if message == 'Uzmobile'and stage_2 == 3.2:
           pass
       if message == 'Mobiuz'and stage_2 == 3.2:
           pass
       if message == 'Ucell'and stage_2 == 3.2:
           pass
       if message == 'Humans'and stage_2 == 3.2:
           pass

       if message == '📍Адреса наших филиалы' and stage_2 == 3 or message == '🎁Yangi chiroyli nomerlar' and stage_2 == 3:
           cur.execute(stagee.format('{}', user_id).format(3.3))
           connect.commit()


    #     Adresla YOOOOOOOOOOOZ LOKATSIYA I RASM I ADRES



       if message == '⚙️Настройки' and stage_2 == 3 or message == '⚙️Sozlamalr' and stage_2 == 3:

           lang_but = [KeyboardButton(text=dct[lang_][3]),
                       KeyboardButton(text=dct[lang_][4])]
           back_but  = [KeyboardButton(text=dct[lang_][0])]
           context.bot.send_message(chat_id=user_id, text=keydct[lang_][3],
                                    reply_markup=ReplyKeyboardMarkup([lang_but,back_but], resize_keyboard=True))
           cur.execute(stagee.format('{}', user_id).format(3.4))
           connect.commit()
       if message == 'Til🇺🇿🇷🇺' and stage_2 == 3.4 or message == 'Язык🇷🇺🇺🇿' and stage_2 == 3.4:
           knopka_lang = [
               InlineKeyboardButton(text='Русский язык🇷🇺', callback_data='ru_change')
           ]
           knopka_lang1 = [
               InlineKeyboardButton(text='''O'zbek tili🇺🇿''', callback_data='uz_change')
           ]
           context.bot.send_message(chat_id=user_id, text='Выберите язык:\nTilni taglang:',
                                    reply_markup=InlineKeyboardMarkup([knopka_lang, knopka_lang1]))
           sleep(1)

       if message == 'Номер телефона☎️' and stage_2 == 3.4 or message == 'Telefon nomer☎️' and stage_2 == 3.4:
           num_ = cur.execute(select_num.format(user_id)).fetchall()
           num_ = num_[0][0]
           cur.execute(stagee.format('{}', user_id).format(3.41))
           connect.commit()
           stage_41 = cur.execute(stage.format(user_id)).fetchall()
           stage_41 = stage_2[0][0]
           # cur.execute(update_phone_num.format(num, user_id))
           # conn.commit()
           if num_ == None and stage_41 == 3.41:
               b = [KeyboardButton(text=dct[lang_][4], request_contact=True)]

               context.bot.send_message(chat_id=user_id, text=dct[lang_][2].format(f_name),
                                        reply_markup=ReplyKeyboardMarkup([b], resize_keyboard=True))
               sleep(1)



       # TIL VA Nomeri



    except Exception:
        pass










def ru(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('user_list.sqlite')
    cur = connect.cursor()
    lang_choose = cur.execute(lang.format('{}', user_id).format(1)).fetchall()
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(2))
    connect.commit()
    k_but = [KeyboardButton(text='далее>>>')]
    context.bot.send_message(text='нажмите на кнопку далее...' , chat_id=user_id, reply_markup= ReplyKeyboardMarkup([k_but], resize_keyboard=True))
    sleep(1)
def uz(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('user_list.sqlite')
    cur = connect.cursor()
    cur.execute(lang.format('{}', user_id).format(2))
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(2))
    connect.commit()
    k_but = [KeyboardButton(text='davom etish>>>')]
    context.bot.send_message(chat_id=user_id, text='davom etamish tugmasini bosing...',  reply_markup= ReplyKeyboardMarkup([k_but], resize_keyboard=True))
    sleep(1)
    print(123)


def ru_change(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('user_list.sqlite')
    cur = connect.cursor()
    lang_choose = cur.execute(lang.format('{}', user_id).format(1)).fetchall()
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(2))
    connect.commit()
    k2_but = [KeyboardButton(text='🏠Главное меню')]
    context.bot.send_message(text='нажмите на кнопку 🏠Главное меню.' , chat_id=user_id, reply_markup= ReplyKeyboardMarkup([k2_but], resize_keyboard=True))
    sleep(1)
def uz_change(update, context):
    user_id = update.callback_query.from_user.id
    connect = sqlite3.connect('user_list.sqlite')
    cur = connect.cursor()
    cur.execute(lang.format('{}', user_id).format(2))
    connect.commit()
    cur.execute(stagee.format('{}', user_id).format(2))
    connect.commit()
    k1_but = [KeyboardButton(text='🏠Asosiy menyu')]
    context.bot.send_message(chat_id=user_id, text='🏠Asosiy menyu tugmasini bosing...',  reply_markup= ReplyKeyboardMarkup([k1_but], resize_keyboard=True))
    sleep(1)
    print(123)




