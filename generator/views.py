from django.shortcuts import render
from django.http import HttpResponse
import random
def home(request):

    return render(request, 'home.html', )

def password(request):
    caracters = list('qwertyuiopasdfghjklzxcvbnm')
    if request.GET.get('number'):
        caracters.extend(list('1234567890'))
    if request.GET.get('uppercase'):
            caracters.extend(list('qwertyuiopasdfghjklzxcvbnm'))
    if request.GET.get('special'):
        caracters.extend(list('~!@#$%^&*()_+'))
    lenght = int(request.GET.get('lenght', 10))

    thepassword = ''
    for x in range(lenght):
        thepassword +=random.choice(caracters)
    context = {'thepassword': thepassword}

    lenght = 10
    return render(request, 'password.html', context)

def about(request):
    return render(request, 'about.html')
