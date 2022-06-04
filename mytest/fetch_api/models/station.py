from django.db import models

# Create your models here.
from django.forms import ModelForm
from django_neomodel import DjangoNode
# from neomodel import StructuredNode, StringProperty, DateProperty
from neomodel import (
    StringProperty,
    StructuredNode,
    RelationshipTo,
    RelationshipFrom,
    Relationship,
    UniqueIdProperty, StructuredRel, FloatProperty
)
class CostShip(StructuredRel):
    pathcost = FloatProperty(default=0.0)


class Station(DjangoNode):
    station_id = UniqueIdProperty(primary_key=True)
    station_name = StringProperty()
    latitude = StringProperty()
    longitude = StringProperty()
    # officers                 = RelationshipFrom('.officer.Officer', 'OFFICER_OF')
    # intermediaries           = RelationshipFrom('.intermediary.Intermediary', 'INTERMEDIARY_OF')
    # addresses                = RelationshipTo('.address.Address', 'REGISTERED_ADDRESS')
    # others                   = RelationshipFrom('.other.Other', 'CONNECTED_TO')
    cost = RelationshipTo('.station.Station', 'FRIEND',model=CostShip)

    class Meta:
        app_label = "fetch_api"
        verbose_name = u'地铁站点信息'
        verbose_name_plural = verbose_name

    @property
    def serialize(self):
        return {
            'node_properties': {
                'station_id': self.station_id,
                'station_name': self.station_name,
                'latitude': self.latitude,
                'longitude': self.longitude,
            },
        }

    @property
    def serialize_connections(self):
        return [
            {
                'nodes_type': 'Station',
                'nodes_related': self.serialize_relationships(self.cost.all())
            },
        ]

class StationForm(ModelForm):
    class Meta:
        model = Station
        fields = ['station_id', 'station_name']