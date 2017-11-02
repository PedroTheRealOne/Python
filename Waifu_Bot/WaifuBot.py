# -*- coding: utf-8 -*-

from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('Waifu')

chat = ['ohayo','ohayo senpai','How r u?','Im fine']

bot.set_trainer(ListTrainer)

bot.train(chat)

while True:
    question = input('Daddy: ')

    response = bot.get_response(question)

    print('Waifu: ', response)
