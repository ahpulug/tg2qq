#!/usr/bin/env python3
'''telegram bot'''

import logging
from telegram.ext import CommandHandler
from telegram.ext import Updater
from telegram.ext import MessageHandler
from telegram.ext import filters


updater = Updater(token="505212073:AAFNhHh4BNCeUUa5GKKZkjpsxr2VJMqbofw")
dispatcher = updater.dispatcher
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)


chat_id_list = []


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
    logging.info("recive command `/start` @id:" +
                 str(update.message.message_id))


@_add_handler(CommandHandler, 'hello')
def hello(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Hello World")
    logging.info("recive command `/hello` @id:" +
                 str(update.message.message_id))


@_add_handler(CommandHandler, "tg2qq")
def tg_2_qq(bot, update):
    logging.info("recive command `/tg2qq` @id:" +
                 str(update.message.message_id))
    chat_id = update.message.chat.id
    if update.message.chat.id not in chat_id_list:
        chat_id_list.append(chat_id)
        logging.info("add chat id :" + str(chat_id))
        logging.info(chat_id_list)
    else:
        logging.warn("this id %s is already in list" % (chat_id))


@_add_handler(MessageHandler, filters.Filters.all)
def recive_message(bot, update):
    logging.info("message from %s :%s" %(update.message.from_user.first_name, update.message.text))


updater.start_polling()
