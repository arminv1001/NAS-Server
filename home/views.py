import os
from django.conf import settings
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
# Create your views here.
login = False

def home(request):
    return render(request, 'home.html', {'name': 'Armin'});


def login(request):
    val1 = request.POST['num1']
    val2 = request.POST['num2']
    if(val1 == "arminv1001"):
        if(val2 == "123456"):
            login = True
            return render(request,'result.html')
    return render(request,'home.html',{'name': ', Passwort oder Benutzername war falsch!'})

def upload(request):
    context = {}
    if request.method == 'POST':
        upload_file = request.FILES['document']
        fs = FileSystemStorage()
        name =  fs.save(upload_file.name, upload_file)
        context['url'] = fs.url(name)
    return render(request, 'result.html', context)

def download(request):
    a = "/Users/armin/Documents/Projekte/EigeneProjekte/NasServer/media"
    liste = {}
    liste['inhalt'] = os.listdir(a)
    print(liste)
    return render(request,'download.html', liste)
#TODO Login