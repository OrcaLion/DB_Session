from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from board.models import Comment

# Create your views here.

@csrf_exempt
def home(request):
    if request.method == 'GET':
        comments = Comment.objects.all();
        return render(request, "home.html", {'comments':comments})
    elif request.method == 'POST':
        Comment.objects.create(
            content = request.POST["content"]
        )
        return redirect("home")
