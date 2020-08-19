import os
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import logout
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.



def home(request):
    return render(request, 'home.html', {'name': 'Armin'});


def log_in(request):
    val1 = request.POST['num1']
    val2 = request.POST['num2']
    user = authenticate(request, username=val1, password=val2)
    if user is not None:
        login(request, user)
        return render(request, 'result.html')
    else:
        return render(request, 'home.html', {'name': ', Passwort oder Benutzername war falsch!'})


def upload(request):
    if not request.user.is_authenticated:
        return render(request, 'home.html', {'name': 'Armin'})
    context = {}
    if request.method == 'POST':
        upload_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(upload_file.name, upload_file)
        context['url'] = fs.url(name)
    return render(request, 'result.html', context)


def download(request):
    if not request.user.is_authenticated:
        return render(request, 'home.html', {'name': 'Armin'})
    a = "/Users/armin/Documents/Projekte/EigeneProjekte/NasServer/media"
    liste = {}
    liste['inhalt'] = os.listdir(a)
    print(liste)
    return render(request, 'download.html', liste)


def log_out(request):
    logout(request)
    return render(request, 'home.html', {'name': 'Armin'})
