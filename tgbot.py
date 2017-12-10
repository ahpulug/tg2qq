#!/usr/bin/env python3
'''telegram bot'''

import logging
import telegram
from telegram.ext import CommandHandler
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import filters


updater = Updater(token="505212073:AAFNhHh4BNCeUUa5GKKZkjpsxr2VJMqbofw")

dispatcher = updater.dispatcher
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)


chat_id_list = []
no_forward_list = []


def _add_handler(handler, filters=None, cmd=None, **kwargs):
    '''just for command and message'''
    def decorater(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        if filter != None:
            '''message handler'''
            func_hander = handler(filters, func, **kwargs)
        elif cmd != None:
            '''command handler'''
            func_hander = handler(cmd, func, **kwargs)
        dispatcher.add_handler(func_hander)
        return wrapper
    return decorater


@_add_handler(CommandHandler, 'start')
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="I'm a bot, please talk to me!")
    logging.info("recive command `/start` @%s" %
                 (update.message.from_user.username))


@_add_handler(CommandHandler, 'hello')
def hello(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Hello World")
    logging.info("recive command `/hello` @%s" %
                 (update.message.from_user.username))


@_add_handler(CommandHandler, "tg2qq")
def tg_2_qq(bot, update):
    logging.info("recive command `/tg2qq` @%s" %
                 (update.message.from_user.username))


    chat_id = update.message.chat.id
    if update.message.chat.id not in chat_id_list:
        chat_id_list.append(chat_id)
        logging.info("add chat id :%s" % (chat_id))
        logging.info("now the chat_list :%s " % (chat_id_list))
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="this id %s has added" % (chat_id))
    else:
        logging.warn("this id %s is already in list" % (chat_id))
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="this id %s is already in list" % (chat_id))


#@_add_handler(CommandHandler,)
@_add_handler(MessageHandler, filters.Filters.all)
def recive_all_message(bot, update):
    """pass"""

    message = update.message

    message_type = get_message_type(message)

    if message_type == "new_menber":
        if message.new_chat_members[0]["id"] == bot.id:
            logging.info("bot joined group \"%s\"" % (message.chat.title))
            return

    if message.chat_id not in chat_id_list:
        logging.warn("A message not from chat queue:user id %s,username %s :%s" %
                     (message.from_user.id, message.from_user.username, message.text))
        return

    if message_type == "leave":
        if message.left_chat_member.id == bot.id:
            logging.info("bot left group \"%s\"" % (message.chat.title))
            return

    full_name = ""
    if message.from_user.first_name:
        full_name += message.from_user.first_name
    if message.from_user.last_name:
        full_name += message.from_user.last_name

    if message_type == "text":
        logging.info("@chat_id %s :a text message from %s :%s" %
                     (message.chat.id, full_name, update.message.text))
        # do something

    else:
        logging.info("@chat_id %s :a %s message from %s" %
                     (message.chat.id, message_type, full_name))


def get_message_type(message={}):
    """ags: update.message

        return: type

    type: text,stickers,photo,voice,video,document"""

    ''''entities': [],
     'caption_entities': [],
      'photo': [],
      'sticker': [] '''
    # print(message)
    if message["text"]:
        return "text"
    elif message["sticker"]:
        return "sticker"
    elif message["photo"]:
        return "photo"
    elif message["voice"]:
        return "voice"
    elif message["video"]:
        return "video"
    elif message["document"]:
        return "document"
    elif message["left_chat_member"]:
        return "leave"
    elif message["new_chat_members"]:
        return "new_menber"
    else:
        logging.warn("a nrecognized message type :%s" % (message))


try:
    updater.start_polling()
except telegram.error.TimedOut:
    print("timeout")
    pass
