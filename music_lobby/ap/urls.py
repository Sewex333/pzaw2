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
    path('album/<int:album_id>/add_to_favorites/', views.add_to_favorites, name='add_to_favorites'),
    path('album/<int:album_id>/remove_from_favorites/', views.remove_from_favorites, name='remove_from_favorites'),
    path('profile/', views.user_profile, name='user_profile'),
    
]
