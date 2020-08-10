from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class BotView(View):
    def post(self, request, *args, **kwargs):
        pass
        return JsonResponse({"ok": "POST request processed"})
