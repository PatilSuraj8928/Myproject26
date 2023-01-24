from django.shortcuts import render

# Create your views here.
from app.models import *

def Display_Topics(request):
    QST=Topic.objects.all()
    d={'Topic':QST}
    return render(request, 'Display_Topics.html',d)

def Display_Webpage(request):
    QSW=Webpage.objects.all()
    d={'Webpages':QSW}
    return render(request, 'Display_Webpage.html',d)

def Display_Access(request):
    QSA=Access_Record.objects.all()
    d={'Access':QSA}
    return render(request, 'Display_Access.html',d)