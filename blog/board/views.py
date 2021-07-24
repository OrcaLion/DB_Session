from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from board.models import Comment, Post

@csrf_exempt
def home(request):
    if request.method == 'GET':
        posts = Post.objects.all();
        return render(request, "home.html", {'posts' : posts})
        
    elif request.method == 'POST':
        print(request.POST["content"])
        Post.objects.create(
            title = request.POST["title"],
            content = request.POST["content"]
        )
        return redirect("home")

@csrf_exempt
def detail(request, pk):
    post = Post.objects.get(pk = pk)

    if request.method == 'GET':
        comments = Comment.objects.filter(
            post = Post.objects.get(pk = pk)
        )

        return render(request, "detail.html", {'post' : post, 'comments' : comments})

    elif request.method == 'POST':
        Comment.objects.create(
            post = post,
            content = request.POST['content']
        )

        return redirect("detail", pk)
