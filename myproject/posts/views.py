from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sayhello(request):
    return HttpResponse('Hello world')

def welcome(request):
    return HttpResponse('<h1 style="color:red; text-align:center;"> Hello User </h1>')

def welcome_user(request, name):
    return HttpResponse(f'<h1 style="color:red; text-align:center;"> Hello {name} </h1>')

def homeuser(request, id):
    return HttpResponse(f'<h1 style="color:red; text-align:center;"> Your id is: {id} </h1>')

def profileview(request):
    message = 'Nice to meet you'
    users = [
        'Omnia', 'Mostafa', 'Basmala', 'Mohamed'
    ]
    return render(request, 'posts/index.html', context={'message':message, 'users': users})