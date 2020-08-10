"""
Command for setting webhook url for telegram API
https://core.telegram.org/bots/webhooks
https://core.telegram.org/bots/self-signed
"""

from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import requests

from telegram.utils import get_api_url


class Command(BaseCommand):
    help = 'Set webhook url for telegram bot'

    def add_arguments(self, parser):
        parser.add_argument('--port', help='Port of the server', type=str, default='443',
                            required=False, choices=['443', '80', '88', '8443'])

    def handle(self, *args, **options):

        payload = {
            'url': get_api_url(options['port']),
        }

        set_webhook_url = f'{settings.TELEGRAM_URL}{settings.BOT_TOKEN}/setWebhook'
        response = requests.post(set_webhook_url, data=payload)
        # response = requests.post(set_webhook_url, files=files, data=payload)
        if response.status_code == 200:
            self.stdout.write(self.style.SUCCESS(
                f'status_code: {response.status_code}, text: {response.text}'))
        else:
            self.stdout.write(self.style.ERROR(
                f'status_code: {response.status_code}, text: {response.text}'))
