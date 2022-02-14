from django.contrib import admin
from .models import Airport, Runway

# Register your models here.
class AirportAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'airport_code', 'is_open']}),
        ('Airport Address', {'fields': ['address', 'city', 'state', 'zipcode'], 'classes': ['collapse']})
    ]

admin.site.register(Airport, AirportAdmin)