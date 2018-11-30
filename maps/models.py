"""
These models are based off of the data structure found here_.  We should change it as we find we aren't using some
fields/models and may need more.  -- Lennon  2018/11/30

.. _here: https://factoriomaps.com/assets/config/maplist.json
"""

from django.db import models


class Map(models.Model):
    name = models.CharField(max_length=256)
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    url = models.URLField()
    preview_url = models.URLField()
    save_url = models.URLField()
    submission_date = models.DateTimeField()
    version = models.IntegerField()
    playtime = models.TimeField()
    ticks = models.BigIntegerField()
    options = models.OneToOneField('maps.Options', on_delete=models.CASCADE)
    save_date = models.DateTimeField()


class Options(models.Model):
    timeline = models.BooleanField()
    image_compression = models.BooleanField()
    modded = models.BooleanField()
    layers = models.IntegerField()
    collapse_layer_list = models.BooleanField()  # Is this really a bool?
    beta = models.BooleanField()
    public_server = models.BooleanField()
    deprecated_top_user = models.BooleanField()
    normal_user = models.BooleanField()


class MapMods(models.Model):
    map = models.ForeignKey('maps.Map', on_delete=models.CASCADE)
    mod = models.ForeignKey('maps.Mod', on_delete=models.SET_NULL, null=True)


class Contributors(models.Model):
    map = models.ForeignKey('maps.Map', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)


class Mod(models.Model):
    name = models.CharField(max_length=256)
