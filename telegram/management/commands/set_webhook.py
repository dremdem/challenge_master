"""
Command for setting webhook url for telegram API
https://core.telegram.org/bots/webhooks
"""

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import requests


class Command(BaseCommand):
    help = 'Set webhook url for telegram bot'

    def add_arguments(self, parser):
        parser.add_argument('--port', help='Port of the server', type=str, default='80',
                            required=False)

    def handle(self, *args, **options):
        port = ''
        # if options['port'] != '80':
        port = f':{options["port"]}'
        set_webhook_url = f'{settings.TELEGRAM_URL}{settings.BOT_TOKEN}' \
                          f'/setWebhook?url={settings.MY_DOMAIN_NAME}{port}/tg/{settings.BOT_TOKEN}'
        response = requests.get(set_webhook_url)
        if response.status_code == 200:
            self.stdout.write(self.style.SUCCESS(
                f'status_code: {response.status_code}, text: {response.text}'))
        else:
            self.stdout.write(self.style.ERROR(
                f'status_code: {response.status_code}, text: {response.text}'))
