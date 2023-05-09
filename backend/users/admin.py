from django.contrib import admin
from django.conf import settings

from .models import User, Follow

admin.site.register(User)
admin.site.register(Follow)
