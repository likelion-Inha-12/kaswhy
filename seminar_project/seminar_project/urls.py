from django.contrib import admin
from django.urls import path, include

from util import views

urlpatterns = [
    path('admin/', admin.site.urls),
		path('health/', views.health),
    path('lion/', include('lionapp.urls'))
]