import os
from django.core.management.base import BaseCommand
from dotenv import load_dotenv
from telegram.ext import Updater
from tgbot.dispatcher import setup_dispatcher


def run_polling(telegram_api_key):
    """ Run bot in polling mode """

    updater = Updater(token=telegram_api_key, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher = setup_dispatcher(dispatcher)
    print("Polling of bot has started")
    updater.start_polling()
    updater.idle()


class Command(BaseCommand):
    help = 'Command for launching a Telegram bot.'

    def handle(self, *args, **kwargs):
        load_dotenv()
        run_polling(os.environ['TG_BOT_HTTP_KEY'])
