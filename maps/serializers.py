from rest_framework import serializers

from maps.models import Map, Mod


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = '__all__'


class ModSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mod
        fields = '__all__'
