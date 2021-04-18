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
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start" start_command))
    dp.add_handler(CommandHandler("start" help_command))

    dp.add_handler(MessageHandler((Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle

main()
