from django.contrib import admin
from django.urls import path
from aplikacja import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Strona główna z menu
]
