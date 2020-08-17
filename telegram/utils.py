"""
Utils for serving telegram API
"""

import requests

from django.conf import settings




def get_webhook_url(port: str = None) -> str:
    """
    Build webook api url
    :param port: custom port
    :return: telegram bot webook url
    """
    if port and port != '443':
        port = f':{port}'
    else:
        port = ''

    return f'{settings.MY_DOMAIN_NAME}{port}/tg/test/'


def send_command(name, data):
    url = f'{settings.BOT_API_URL}{name}'
    return requests.post(url, json=data)


def set_commands():
    bot_commands = [
        {'command': 'start', 'description': 'start command'},
        {'command': 'help', 'description': 'This is help!'},
        {'command': 'test', 'description': 'this is test'},
    ]

    data = {
        'commands': bot_commands
    }

    return send_command('setMyCommands', data)


def send_message(chat_id, message):
    # data = {
    #     "chat_id": chat_id,
    #     "text": message,
    #     "parse_mode": "Markdown"
    # }

    data = {
        "chat_id": chat_id,
        "text": message,
        "parse_mode": "Markdown",
        "reply_markup": {
            "keyboard": [[
                {"text": "/start"},
                {"text": "/help"},
                {"text": "/description"},
            ]],
            "one_time_keyboard": True
        }
    }

    send_command("sendMessage", data)


