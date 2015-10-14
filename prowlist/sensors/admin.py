from django.contrib import admin
from .models import *

#admin.site.register(Sensor)
admin.site.register(SensorLogs)


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
	list_display = ('name', 'uuid', 'serial', 'active')
	search_fields = ['serial', 'name']