from django.contrib import admin
from .models import Post
from .models import Photos

@admin.register(Photos)
class PhotoAdmin(admin.ModelAdmin):
    model = Photos


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post

