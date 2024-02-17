import os
from dotenv import load_dotenv
from telegram.ext import Updater
from dispatcher import setup_dispatcher


def run_polling(telegram_api_key):
    """ Run bot in polling mode """

    updater = Updater(token=telegram_api_key, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher = setup_dispatcher(dispatcher)

    print("Polling of bot has started")

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    load_dotenv()
    telegram_api_key = os.environ['TG_BOT_HTTP_KEY']
    run_polling(telegram_api_key)
