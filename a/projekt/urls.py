from django.urls import path
from . import views

urlpatterns = [
    path('', views.club_list, name='club_list'),
    path('club/<int:club_id>/', views.club_detail, name='club_detail'),
    path('player/<int:player_id>/', views.player_detail, name='player_detail'),
    path('player/<int:player_id>/add_comment/', views.add_comment, name='add_comment'),
]
