from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import requests


class Command(BaseCommand):
    help = 'Set webhook url for telegram bot'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        set_webhook_url = f'{settings.TELEGRAM_URL}{settings.BOT_TOKEN}' \
                          f'/setWebhook?url={settings.MY_DOMAIN_NAME}/tg/{settings.BOT_TOKEN}'
        response = requests.get(set_webhook_url)
        if response.status_code == 200:
            self.stdout.write(self.style.SUCCESS(
                f'status_code: {response.status_code}, text: {response.text}'))
        else:
            self.stdout.write(self.style.ERROR(
                f'status_code: {response.status_code}, text: {response.text}'))
