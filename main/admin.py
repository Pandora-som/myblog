from django.contrib import admin

from .models import User, State, Comment

admin.site.register(User)
admin.site.register(State)
admin.site.register(Comment)

# Register your models here.
