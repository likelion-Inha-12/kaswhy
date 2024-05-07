from django.contrib import admin

from .models import Post, Comment, Member

# Register your models here.
admin.site.register(Member)
admin.site.register(Post)
admin.site.register(Comment)
# admin.site.register(UserPost)