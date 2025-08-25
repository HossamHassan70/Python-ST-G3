from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

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
    return render(request, 'posts/index.html', context={'mymessage':message, '  ': users})

our_posts = [
    {'id': 1, 'title': 'Post1', 'description': 'This is the description for post1'},
    {'id': 2, 'title': 'Post2', 'description': 'This is the description for post2'},
    {'id': 3, 'title': 'Post3', 'description': 'This is the description for post3'},
]
def indexposts(request):
    return render(request, 'posts/posts.html', context={'posts': our_posts})

def showpost(request, id):
    for post in our_posts:
        if post['id'] == id:
            return render(request, 'posts/show.html', context={'post': post})
    else:
        return HttpResponse('Post Not Found')

def allposts(request):
    post_list = Post.objects.all()
    context = {'my_list': post_list}
    return render(request, 'posts/allposts.html', context)

def post_detail(request, id):
    p_detail = Post.objects.get(id = id)
    context = {'post_detail': p_detail}
    return render(request, 'posts/post_detail.html', context)