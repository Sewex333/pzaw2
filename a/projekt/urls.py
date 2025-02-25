from django.urls import path
from . import views

urlpatterns = [
    path('', views.album_list, name='album_list'),
    path('album/<int:album_id>/', views.album_detail, name='album_detail'),
    path('track/<int:track_id>/', views.track_detail, name='track_detail'),
    path('track/<int:track_id>/add_comment/', views.add_comment, name='add_comment'),
]
