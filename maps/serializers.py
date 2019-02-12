from rest_framework import serializers

from maps.models import Map, Mod


class MapSerializer(serializers.ModelSerializer):
    """A simple map serializer"""
    class Meta:
        model = Map
        fields = '__all__'


class ModSerializer(serializers.ModelSerializer):
    """A simple mod serializer"""
    class Meta:
        model = Mod
        fields = '__all__'
