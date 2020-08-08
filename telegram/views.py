from django.shortcuts import render
from django.views import View
from django.http import JsonResponse


class BotView(View):
    def post(self, request, *args, **kwargs):
        pass
        return JsonResponse({"ok": "POST request processed"})
