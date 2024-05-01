from django.contrib import admin
from django.urls import path

from lionapp import views

from . import views

urlpatterns = [
    path('create/', views.create_post),
    path('<int:pk>/', views.get_post),
    path('delete/<int:pk>', views.delete_post),
    path('comments/<int:post_id>', views.get_comment),
    path('like/<int:user_id>/<int:post_id>', views.like),
    path('')
]