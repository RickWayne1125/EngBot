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
| /en [TEXT]       | From Chinese to English                                    | Basic Finish                 |
| /zh [TEXT]       | From English to Chinese                                    | Basic Finish                 |
| ~~/show [WORD]~~ | Search the meaning of the word in dictionary               | Integrated in translate part |
| /add [WORD]      | Add the word to your list                                  | On going                     |
| /remove [WORD]   | Remove the word from your list                             | On going                     |
| /review [NUM]    | Choose a number of random words to review                  | On going                     |
| /daily           | Random daily English contents (Famous lines, lyrics, etc.) | To do                        |

## Configurations

Configurations are set in the `config.py` file.

配置文件存放于`config.py`文件中。

```python
tgbot = {
    'token': 'TOKEN'
}
youdao = {
    'url': 'https://openapi.youdao.com/api',
    'app_id': 'APP ID',
    'app_secret': 'APP SECRET'
}
```

