from django.contrib import admin
from .models import Airport, Runway

# Register your models here.
class RunwayInline(admin.StackedInline):
    model = Runway  # Specify which model to use
    extra = 2  # How many to start with

class AirportAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'airport_code', 'is_open']}),
        ('Airport Address', {'fields': ['address', 'city', 'state', 'zipcode'], 'classes': ['collapse']})
    ]
    inlines = [RunwayInline]  # Load the RunwayInLine Class

admin.site.register(Airport, AirportAdmin)