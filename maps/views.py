"""Views for the Maps app."""
# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from maps.models import Map, Mod
from maps.serializers import (
    MapSerializer,
    ModSerializer,
)


class MapViewSet(viewsets.ModelViewSet):
    """A RESTful API for Maps"""
    queryset = Map.objects.all()
    serializer_class = MapSerializer
    permission_class = [AllowAny]


class ModViewSet(viewsets.ModelViewSet):
    """A RESTful API for Mods"""
    queryset = Mod.objects.all()
    serializer_class = ModSerializer
    permission_classes = [AllowAny]
