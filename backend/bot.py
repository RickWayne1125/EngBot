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


def start(update: Update, context: CallbackContext) -> int:
    """
    Start the conversation and ask user for input.
    """
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hi! My name is Eng Bot. I will help you learn english.\n你好！我是英语机器人！我会帮助你学习英语。"
    )


def formatter(text: Dict) -> str:
    res = text['query'] + '\n' + '\n'
    if(not text['isWord']):
        res += '翻译结果：' + text['translation'] + '\n'
        res += '\n'
    else:
        res += '词典释义：' + '\n'
        for i in text['basic']['explains']:
            res += i + '\n'
        res += '\n'
    if(text.__contains__('web')):
        res += '网络释义：' + '\n'
        for i in text['web']:
            key = i['key']
            value = ','.join(i['value'])
            res += key + ': ' + value + '\n'
        res += '\n'
    res += 'Add to list: ' + '/add ' + text['query']
    return res


def en2zh(update, context):
    text = ' '.join(context.args)
    print(text)
    res = connect(text, 'en', 'zh-CHS')
    res = formatter(res)
    context.bot.send_message(chat_id=update.effective_chat.id, text=res)


def zh2en(update, context):
    text = ' '.join(context.args)
    res = connect(text, 'zh-CHS', 'en')
    res = formatter(res)
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
