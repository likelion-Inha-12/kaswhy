from django.contrib import admin

from .models import Post, Comment, Member, UserPost

# Register your models here.
admin.site.register(Member)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserPost)