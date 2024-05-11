from django.shortcuts import render
from django.http import HttpResponse
from .models import Services, Portfolio, About, Team, Contact


# Create your views here.
def index(request):
    categories = Services.objects.filter(is_visible=True)
    return render(request, 'index.html')

def index2(request):
    categories = Portfolio.objects.filter(is_visible=True)
    return render(request, 'index.html')

def index3(request):
    categories = About.objects.filter(is_visible=True)
    return render(request, 'index.html')

def index4(request):
    categories = Team.objects.filter(is_visible=True)
    return render(request, 'index.html')

