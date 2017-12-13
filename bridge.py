import os
import sys

from qqbot.utf8logger import CRITICAL, ERROR, WARN, INFO, DEBUG

class Bridge(object):

    def __init__(self):
        self.qq_bot = None
        self.tg_bot = None

    def add_qq(self, bot):
        self.qq_bot = bot

    def add_tg(self, bot):
        self.tg_bot = bot

    def add_qq_contact(self,contact):
        self.qq_contact = contact
        INFO(self.qq_contact)
        INFO(type(self.qq_contact))

    def add_tg_chat_id(self,chat_id):
        self.chat_id = chat_id

    def send_to_qq(self, menber, content):
        INFO("send to qq %s" %(content))
        #contact = "群“test”"
        self.qq_bot.SendTo(self.qq_contact, menber +" :" + content )

    def send_to_tg(self, menber, content):
        INFO("send to tg %s" %(content))
        INFO(type(self.tg_bot.sendMessage))
        self.tg_bot.sendMessage(chat_id=self.chat_id,
                        text="%s :%s" % (menber,content))

test = Bridge()
main_bridge = test
