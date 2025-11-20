from django.contrib import admin
from .models import user,admin_user,employee_user,scan_card,schedule_meeting

# Register your models here.
admin.site.register(user)
admin.site.register(admin_user)
admin.site.register(employee_user)
admin.site.register(scan_card)
admin.site.register(schedule_meeting)