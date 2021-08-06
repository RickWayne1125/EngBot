# EngBot
> 🤖 A Telegram Bot for Chinese speakers to learn English
>
> 🤖 一个用来给中文使用者学习英语的电报机器人

目前翻译模块使用有道翻译的 API

词典模块可能使用离线词典/有道词典的形式

## Basic Functions
Including:

| Name             | Description                                                | Schedule                     |
| ---------------- | ---------------------------------------------------------- | ---------------------------- |
| /en [TEXT]       | From Chinese to English                                    | Basically Finished           |
| /zh [TEXT]       | From English to Chinese                                    | Basically Finished           |
| /show            | Show all the words in your list                            | Basically Finished           |
| /add [WORD]      | Add the word to your list                                  | Basically Finished           |
| /remove [WORD]   | Remove the word from your list                             | Basically Finished           |
| /review [NUM]    | Choose a number of random words to review                  | Adding Q&A Functtion         |
| /daily           | Random daily English contents (Famous lines, lyrics, etc.) | To do                        |

## Configurations

Configurations are set in the `config.py` file.

配置文件存放于`config.py`文件中。

```python
tgbot = {
    'token': 'TOKEN'	#Telegram Bot Token From @BotFather
}
youdao = {
    'url': 'https://openapi.youdao.com/api',
    'app_id': 'APP ID',	#APP ID From YouDao Open API
    'app_secret': 'APP SECRET'	# APP Secret Key From YouDao Open API
}
```

