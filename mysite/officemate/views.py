from django.shortcuts import render

from django.http import HttpResponse

from .models import Post, Comments, Reply

def index(request):
    posts = Post.objects.all()
    comments = Comments.objects.all()
    replies = Reply.objects.all()

    context = {
        'posts': posts,
        'comments': comments,
        'replies': replies,
    }
    return render(request, 'base.html', context)


