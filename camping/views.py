from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import (
    PostForm, 
)

from .models import Post, Photos

def index(request):
    post_list = Post.objects.all()
    image_list = Photos.objects.all()
    context = {
        "post_list" : post_list,
        "image_list" : image_list,
    }
    return render(request, "camping/index.html", context)


@login_required
def create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            for image in request.FILES.getlist("images"):
                photo = Photos()
                photo.post = post
                photo.image = image
                photo.save()

            return redirect("camping:index")
        
    else:
        form = PostForm()
        context = {
            "form" : form,
        }
        return render(request, "camping/create.html", context)

@login_required
def update(request, pk):
    instance = Post.objects.filter(pk=pk).first()
    if request.method == "POST":
        form = PostForm(instance, request.POST, request.FILES)
        return 
    else:
        form = PostForm(instance)




def detail(request, pk):
    post = Post.objects.filter(pk=pk).first()

    context = {
        "post" : post
    }
    return render(request, "camping/detail.html", context)