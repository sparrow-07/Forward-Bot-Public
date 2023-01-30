import logging

from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

API_KEY = "please enter your api key here"

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO) logger = logging.getLogger(__name__)

class Bot:
    def __init__(self):
        updater = Updater(API_KEY)
        self.__bot = updater.bot

        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler("start", self.receive_command, pass_user_data=True))
        dispatcher.add_handler(MessageHandler(Filters.text, self.receive_message, pass_user_data=True))

        updater.start_polling()

    def receive_command(self, bot, update, user_data):
        print(update.message.id)

    def receive_message(self, bot, update, user_data):
        print(update.message.id)

Bot()
