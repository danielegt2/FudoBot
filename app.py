#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    FudoBot
    lista comandi:
    
help - ok.jpg
milan - andré sola
dollarumma - $
crudeli - boa! teng! teng! teng!
pogba - 30!
switch - modalità molesta on/off
    
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging, re

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    update.message.reply_text('A regazzì, e mo vo buco sto pallone')
    
def herupu(bot, update):
    update.message.reply_text('Nella modalità molesta non è necessario inserire /<comando> per attivare il bot')

def milan(bot, update):
    update.message.reply_photo("https://www.calciomercato.it/imagesArticleBig/6/8/0/d/185332.jpg")

def dollarumma(bot, update):
    update.message.reply_photo('https://content.fantagazzetta.com/web/img/1150x532/7ee14989-af70-4bd9-8b18-e4e58bf6c0d2.jpg')

def crudeli(bot, update):
    update.message.reply_photo('http://www.cittaceleste.it/wp-content/uploads/sites/6/2015/10/CRUDELI23.jpg')

def pogba(bot, update):
    update.message.reply_text('30!')

def scan(bot, update):
    keywords = ['milan','dollarumma','donnarumma','crudeli','pogba']
    for i, v in enumerate(keywords):
        match = re.search(r'\b{}\b'.format(v) , update.message.text, flags=re.IGNORECASE)
        if match:
            if i == 0:
                milan(bot, update)
            elif 1 <= i <= 2:
                dollarumma(bot,update)
                print(i)
            elif i == 3:
                crudeli(bot, update)
            else:
                pogba(bot,update)


def switch(bot, update):
    global dp
    global molesta
    global scanhandler
    if molesta == True:
        molesta = False
        dp.remove_handler(scanhandler)
        update.message.reply_text('modalità molesta OFF')
    else:
        molesta = True
        dp.add_handler(scanhandler)
        update.message.reply_text('modalità molesta ON')

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("664394810:AAEQ1dVh2UoHdDtBz3aHplTrKIRDyPgBuuA")

    # Get the dispatcher to register handlers
    global dp
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", herupu))
    dp.add_handler(CommandHandler("milan", milan))
    dp.add_handler(CommandHandler("pogba", pogba))
    dp.add_handler(CommandHandler("dollarumma", dollarumma))
    dp.add_handler(CommandHandler("crudeli", crudeli))
    global molesta
    molesta = True
    global scanhandler
    scanhandler = MessageHandler(Filters.text, scan)
    dp.add_handler(scanhandler)
    dp.add_handler(CommandHandler("switch", switch))
    
    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
