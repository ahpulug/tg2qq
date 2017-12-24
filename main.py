import os
import threading

import qqbot
import tgbot
from qqbot import _bot as qq_bot
from utf8logger import INFO


class Bot_thread(threading.Thread):
    """I dont think it should be stop xd"""

    def __init__(self, thread_func):
        threading.Thread.__init__(self)
        self.thread_func = thread_func

    def run(self):
        INFO(self.thread_func.__name__ + " running...")
        subthread = threading.Thread(target=self.thread_func)
        subthread.start()
        subthread.join()


def tg_bot_run():
    tgbot.Main()


def qq_bot_run():
    qqbot.Main()


if __name__ == "__main__":
    tg_thread = Bot_thread(thread_func=tg_bot_run)
    qq_thread = Bot_thread(thread_func=qq_bot_run)

    tg_thread.run()
    qq_thread.run()
