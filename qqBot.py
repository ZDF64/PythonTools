from qqbot import QQBotSlot as qqbotslot, RunBot

@qqbotslot
def onQQMessage(bot, contact, member, content):
    if contact.ctype == 'group' and content == 'hello':
        bot.SendTo(contact, 'world')

if __name__ == '__main__':
    RunBot()