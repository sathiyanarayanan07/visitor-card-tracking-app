from django.contrib import admin
from .models import user,admin_user

# Register your models here.
admin.site.register(user)
admin.site.register(admin_user)
