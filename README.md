# EngBot
> 🤖 A Telegram Bot for Chinese speakers to learn English
>
> 🤖 一个用来给中文使用者学习英语的电报机器人

目前翻译模块使用有道翻译的 API

词典模块可能使用离线词典/有道词典的形式

## Basic Functions
Including:

| Name           | Description                                  |
| -------------- | -------------------------------------------- |
| /en [TEXT]     | From Chinese to English                      |
| /cn [TEXT]     | From English to Chinese                      |
| /show [WORD]   | Search the meaning of the word in dictionary |
| /add [WORD]    | Add the word to your list                    |
| /remove [WORD] | Remove the word from your list               |

## Configurations

Configurations are set in the `config.py` file.

配置文件存放于`config.py`文件中。

```python
telegram = {
    'token': 'TOKEN'
}
youdao = {
    'url': 'https://openapi.youdao.com/api',
    'app_id': 'APP ID',
    'app_secret': 'APP SECRET'
}
```

