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
    PicklePersistence
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


def en2zh(update: Update, context: CallbackContext):
    text = ' '.join(context.args)
    print(text)
    res = connect(text, 'en', 'zh-CHS')
    res = formatter(res)
    context.bot.send_message(chat_id=update.effective_chat.id, text=res)


def zh2en(update: Update, context: CallbackContext):
    text = ' '.join(context.args)
    res = connect(text, 'zh-CHS', 'en')
    res = formatter(res)
    context.bot.send_message(chat_id=update.effective_chat.id, text=res)


def add(update: Update, context: CallbackContext):
    text = ' '.join(context.args)
    msg = text
    if context.user_data.__contains__('list'):
        if context.user_data['list'].__contains__(text):
            msg += ': Already Added!'
        else:
            res = connect(text, 'en', 'zh-CHS')
            context.user_data['list'].setdefault(text, res)
            msg += ': Successfully Added!'
    else:
        context.user_data['list'] = {}
        msg = 'List Created Successfully!\n'
        res = connect(text, 'en', 'zh-CHS')
        context.user_data['list'].setdefault(text, res)
        msg = text + ': Successfully Added!'
    context.bot.send_message(chat_id=update.effective_chat.id, text=msg)


def show(update: Update, context: CallbackContext):
    if context.user_data.__contains__('list'):
        for i in context.user_data['list'].values():
            msg = formatter(i)
            context.bot.send_message(
                chat_id=update.effective_chat.id, text=msg)
    else:
        return None


def remove(update: Update, context: CallbackContext):
    if context.user_data.__contains__('list'):
        text = ' '.join(context.args)
        if context.user_data['list'].__contains__(text):
            del context.user_data['list'][text]
        context.bot.send_message(
            chat_id=update.effective_chat.id, text=text+': Successfully Removed!')
    else:
        return None


def main(token) -> None:
    """Run the bot."""
    # Create the Updater and pass it your bot's token.
    persistence = PicklePersistence(filename='engbotdb')
    updater = Updater(token, persistence=persistence)

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

    # Add list-control handler
    add_handler = CommandHandler('add', add)
    dispatcher.add_handler(add_handler)
    show_handler = CommandHandler('show', show)
    dispatcher.add_handler(show_handler)
    remove_handler = CommandHandler('remove', remove)
    dispatcher.add_handler(remove_handler)

    # Start the Bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    token = tgbot['token']
    main(token)
