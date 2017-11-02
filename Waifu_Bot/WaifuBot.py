# -*- coding: utf-8 -*-

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Waifu')

chatI = ['ohayo','ohayo senpai','Supp','How rude','How are you?','Im fine','Senpai, What are you doing?', 'I love you senpai']

chatT = ['Im just waiting you', 'Thanks', 'How was your day, Senpai?']

chatQ = ['What do you like to eat?','What do you like to do?']

chatR = ['Senapi, untie me please.']

chatDump = ['You are scarring me']

bot.set_trainer(ListTrainer)

bot.train(chatI)
bot.train(chatT)
bot.train(chatQ)
bot.train(chatR)
bot.train(chatDump)

while True:
    question = input('Daddy: ')

    response = bot.get_response(question)
    
    if float(response.confidence) > 0.5:
        print('Waifu: ', response)
    else:
        print('Waifu: ', response)
