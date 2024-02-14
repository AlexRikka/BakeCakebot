import argparse
import telegram
import time
import os
import random
from dotenv import load_dotenv, find_dotenv


if __name__ == "__main__":
    load_dotenv(find_dotenv())
    tg_token = os.getenv("TG_TOKEN")
    chat_id = os.getenv("CHAT_ID")
    directory = os.getenv("DIRECTORY")
    bot = telegram.Bot(token=tg_token)
