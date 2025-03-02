from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('album/<int:album_id>/', views.album_detail, name='album_detail'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('album/<int:album_id>/rate/', views.rate_album, name='rate_album'),
    path('album/<int:album_id>/comment/', views.add_comment, name='add_comment'),
]
