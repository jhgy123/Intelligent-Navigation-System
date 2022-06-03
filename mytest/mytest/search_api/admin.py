from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django_neomodel import admin as neo_admin

from .models import Station
#  from .address import Address
#  from .intermediary import Intermediary
#  from .officer import Officer
#  from .other import Other

# class StationAdmin(admin.ModelAdmin):
#     list_display = ("station_id",)
# admin.site.register(Station, StationAdmin)

# For easily access each of the model classes programmatically, create a key-value map.
MODEL_ENTITIES = {
    'Station': Station
}