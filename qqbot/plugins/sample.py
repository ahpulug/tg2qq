# -*- coding: utf-8 -*-

# 插件加载方法： 
# 先运行 qqbot ，启动成功后，在另一个命令行窗口输入： qq plug qqbot.plugins.sample

from bridge import main_bridge

def onQQMessage(bot, contact, member, content):
    if content == '/start':
        bot.SendTo(contact, '你好，我是QQ机器人')
    elif content == '/stop':
        bot.SendTo(contact, 'QQ机器人已关闭')
        bot.Stop()
    elif content == '/qq2tg':
        bot.SendTo(contact, 'qq to tg')
        main_bridge.add_qq_contact(contact)
        main_bridge.add_qq(bot)

    else:
        main_bridge.send_to_tg(member,content)
