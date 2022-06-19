from django.contrib import admin as dj_admin
from django_neomodel import admin as neo_admin

# from search_api.models import Station
from .models import Entity, Station


#  from .address import Address
#  from .intermediary import Intermediary
#  from .officer import Officer
#  from .other import Other

# class EntityAdmin(dj_admin.ModelAdmin):
#     list_display = ("name",)
# neo_admin.register(Entity, EntityAdmin)
class StationAdmin(dj_admin.ModelAdmin):
    list_display = ("station_id","station_name","latitude","longitude","is_transit")
neo_admin.register(Station, StationAdmin)