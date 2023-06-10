from django.shortcuts import render

from .models import Team

# Create your views here.
def index(request):
    context = {
        "teams": Team.objects.order_by("-pts")
    }
    return render(request, 'index.html', context=context)