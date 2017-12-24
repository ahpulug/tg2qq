import os
import sys

p = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if p not in sys.path:
    sys.path.insert(0, p)

sys.path.append('../')


from tgbot.botUpdate import run
from tgbot import Main

Main()
