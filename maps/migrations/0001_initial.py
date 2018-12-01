# Generated by Django 2.1.3 on 2018-12-01 11:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('url', models.URLField()),
                ('preview_url', models.URLField()),
                ('save_url', models.URLField()),
                ('submission_date', models.DateTimeField()),
                ('version', models.IntegerField()),
                ('factorio_version', models.CharField(max_length=16)),
                ('ticks', models.BigIntegerField()),
                ('save_date', models.DateTimeField()),
                ('timeline', models.BooleanField()),
                ('image_compression', models.BooleanField()),
                ('modded', models.BooleanField()),
                ('layers', models.IntegerField()),
                ('collapse_layer_list', models.BooleanField()),
                ('beta', models.BooleanField()),
                ('public_server', models.BooleanField()),
                ('deprecated_top_user', models.BooleanField()),
                ('normal_user', models.BooleanField()),
                ('contributors', models.ManyToManyField(blank=True, related_name='contributors', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('title', models.CharField(max_length=256)),
                ('version', models.CharField(max_length=16)),
                ('file', models.FileField(upload_to='files/mods/')),
            ],
        ),
        migrations.AddField(
            model_name='map',
            name='mods',
            field=models.ManyToManyField(blank=True, to='maps.Mod'),
        ),
        migrations.AddField(
            model_name='map',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]