"""
Utils for serving telegram API
"""

from django.conf import settings


def get_api_url(port=None):
    if port and port != '443':
        port = f':{port}'
    else:
        port = ''

    return f'{settings.MY_DOMAIN_NAME}{port}/tg/test/'
