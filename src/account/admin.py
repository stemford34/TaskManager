from django.contrib import admin

from .models import User, EmailActivation


admin.site.register(User)
admin.site.register(EmailActivation)