from django.contrib import admin
from django.urls import path

from lionapp import views

from . import views

urlpatterns = [
    path('create/', views.create_post),
    path('<int:pk>/', views.get_post),
    path('delete/<int:pk>', views.delete_post),
    path('comments/<int:post_id>', views.get_comment),
#    path('like/', views.like),
#    path('getlike/<int:post_id>', views.get_like),
    path('v2/post/<int:pk>',views.PostApiView.as_view()),
    path('v2/post',views.create_post_v2)
]