from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html', {'name': 'Armin'});


def add(request):
    val1 = request.POST['num1']
    val2 = request.POST['num2']
    if(val1 == "arminv1001"):
        if(val2 == "123456"):
            res = "true"
            return render(request,'result.html')

    return render(request,'home.html',{'name': ', Passwort oder Benutzername war falsch!'})