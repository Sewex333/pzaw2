from django.contrib import admin
from .models import User
from .models import Game, Question, Category

admin.site.register(Game)
admin.site.register(Question)
admin.site.register(Category)
admin.site.register(User)