from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('stats/', views.stats, name='stats'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('settings/', views.settings_view, name='settings'),
    path('start_game/', views.start_game, name='start_game'),
    path('game/<int:game_id>/', views.game_view, name='game'),
    path('game/<int:game_id>/question/<int:question_id>/', views.question_view, name='question')
]

