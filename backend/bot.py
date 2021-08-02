import config

from translate import connect

import logging
from typing import Dict

from telegram import ReplyKeyboardMarkup, Update, ReplyKeyboardRemove
import telegram
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

from config import tgbot

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

# reply_keyboard = [
#     ['英译汉', '汉译英'],
#     ['收藏单词', '移除单词'],
#     ['Done'],
# ]
# markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)


def start(update: Update, context: CallbackContext) -> int:
    """
    Start the conversation and ask user for input.
    """
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hi! My name is Eng Bot. I will help you learn english.\n你好！我是英语机器人！我会帮助你学习英语。"
    )


def en2zh(update, context):
    text = str(context.args)
    res = str(connect(text, 'en', 'zh-CHS').decode())
    context.bot.send_message(chat_id=update.effective_chat.id, text=res)


def zh2en(update, context):
    text = str(context.args)
    res = str(connect(text, 'zh-CHS', 'en').decode())
    context.bot.send_message(chat_id=update.effective_chat.id, text=res)


def main(token) -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Add start handler
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Add translate handler
    en2zh_handler = CommandHandler('zh', en2zh)
    zh2en_handler = CommandHandler('en', zh2en)
    dispatcher.add_handler(en2zh_handler)
    dispatcher.add_handler(zh2en_handler)

    # Start the Bot
    updater.start_polling()


if __name__ == '__main__':
    token = tgbot['token']
    main(token)
