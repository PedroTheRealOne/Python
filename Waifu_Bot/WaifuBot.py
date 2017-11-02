# -*- coding: utf-8 -*-

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Waifu')

chatI = ['ohayo','ohayo senpai','How r u?','Im fine','Senpai, What are you doing?']

chatT = ['Im just waiting you', 'Thanks']

chatDump = ['You are scarring me']

bot.set_trainer(ListTrainer)

bot.train(chatI)
bot.train(chatDump)
bot.train(chatT)

while True:
    question = input('Daddy: ')

    response = bot.get_response(question)
    
    if float(response.confidence) > 0.5:
        print('Waifu: ', response)
    else:
        print('Waifu: ', response)
