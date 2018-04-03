from django.shortcuts import render
from .models import WildMagicSurgeEffect
import random

def index(request):
    effect = WildMagicSurgeEffect.objects.get(id=random.randint(1,3))
    # effects = WildMagicSurgeEffect.objects.order_by('id')[:3]
    return render(request, 'wmsg/index.html', {'effect': effect})
