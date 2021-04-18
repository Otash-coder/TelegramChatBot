import constants as keys
from telegram.ext import *
import responces as responce

print("Bot started...")


def start_command(update, context):
    update.message.reply_text('Type someyhing random to get started!')


def help_command(update, context):
    update.message.reply_text('If you need help! Google it!')


def handle_message(update, context):
    text = str(update.message.text).lower()
    responce = R.sample_responces(text)

    update.message.reply_text(responce)


def error(update, context):
