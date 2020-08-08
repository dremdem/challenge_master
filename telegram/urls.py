from django.conf import settings
from django.urls import path
from telegram.views import BotView


urlpatterns = [
       path(f'{settings.BOT_TOKEN}', BotView.as_view()),
]

