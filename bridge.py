from utf8logger import CRITICAL, ERROR, WARN, INFO, DEBUG


class Bridge(object):

    def __init__(self):
        self.qq_bot = None
        self.tg_bot = None
        self.chat_id = []
        self.qq_contact = []


    def add_qq(self, bot):
        self.qq_bot.append(bot)

    def add_tg(self, bot):
        self.tg_bot.append(bot)

    def add_qq_contact(self,contact):
        self.qq_contact.append(contact)

    def add_tg_chat_id(self,chat_id):
        self.chat_id.append(chat_id)

    def send_to_qq(self, menber, content):
        INFO("send to qq %s" %(content))
        for contact in self.qq_contact:
            self.qq_bot.SendTo(contact, menber +" :" + content )

    def send_to_tg(self, menber, content):
        INFO("send to tg %s" %(content))
        for _chat_id in self.chat_id:
            self.tg_bot.sendMessage(chat_id=_chat_id,
                            text="%s :%s" % (menber,content))
