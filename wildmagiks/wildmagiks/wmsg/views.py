from django.http import HttpResponse
from .models import WildMagicSurgeEffect

def index(request):
    effect = WildMagicSurgeEffect.objects.get(id="2")
    return HttpResponse(effect)
