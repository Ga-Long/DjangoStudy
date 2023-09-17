from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'content', 'created_at','view_count', 'likes', 'writer')

admin.site.register(Post, PostAdmin)