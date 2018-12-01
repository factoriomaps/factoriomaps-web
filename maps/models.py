"""
These models are based off of the data structure found here_.  We should change it as we find we aren't using some
fields/models and may need more.  -- Lennon  2018/11/30

.. _here: https://factoriomaps.com/assets/config/maplist.json
"""

from django.db import models


class Map(models.Model):
    def __str__(self):
        return f'{self.user}_{self.name}_{self.submission_date}'
    name = models.CharField(max_length=256)
    user = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True, related_name='user')
    url = models.URLField()
    preview_url = models.URLField()
    save_url = models.URLField()
    submission_date = models.DateTimeField()
    version = models.IntegerField()
    factorio_version = models.CharField(max_length=16)
    ticks = models.BigIntegerField()
    save_date = models.DateTimeField()
    timeline = models.BooleanField()
    image_compression = models.BooleanField()
    modded = models.BooleanField()
    layers = models.IntegerField()
    collapse_layer_list = models.BooleanField()  # Is this really a bool?
    beta = models.BooleanField()
    public_server = models.BooleanField()
    deprecated_top_user = models.BooleanField()
    normal_user = models.BooleanField()
    mods = models.ManyToManyField('maps.Mod', blank=True)
    contributors = models.ManyToManyField('auth.User', blank=True, related_name='contributors')


class Mod(models.Model):
    def __str__(self):
        return f'{self.name}_{self.version}'
    name = models.CharField(max_length=256) # exact name from mod portal e.g. "bobores"
    title = models.CharField(max_length=256) # mod title e.g. "Bob's Ores"
    version = models.CharField(max_length=16)
    file = models.FileField(upload_to='files/mods/')
