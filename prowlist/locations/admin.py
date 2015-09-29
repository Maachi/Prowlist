from django.contrib import admin
from locations.models import *

admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Location)
