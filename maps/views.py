# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from maps.models import Map, Options, MapMods, Contributors, Mod
from maps.serializers import (
    MapSerializer,
    OptionsSerializer,
    MapModsSerializer,
    ContributorsSerializer,
    ModSerializer,
)


class MapViewSet(viewsets.ModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializer
    permission_class = [AllowAny]


class OptionsViewSet(viewsets.ModelViewSet):
    queryset = Options.objects.all()
    serializer_class = OptionsSerializer
    permission_class = [AllowAny]


class MapModsViewSet(viewsets.ModelViewSet):
    queryset = MapMods.objects.all()
    serializer_class = MapModsSerializer
    permission_class = [AllowAny]


class ContributorsViewSet(viewsets.ModelViewSet):
    queryset = Contributors.objects.all()
    serializer_class = ContributorsSerializer
    permission_class = [AllowAny]


class ModViewSet(viewsets.ModelViewSet):
    queryset = Mod.objects.all()
    serializer_class = ModSerializer
    permission_classes = [AllowAny]