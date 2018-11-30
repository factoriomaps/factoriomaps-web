from rest_framework import serializers

from maps.models import Map, Options, MapMods, Contributors, Mod


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = '__all__'


class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = '__all__'


class MapModsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapMods
        fields = '__all__'


class ContributorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributors
        fields = '__all__'


class ModSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mod
        fields = '__all__'
