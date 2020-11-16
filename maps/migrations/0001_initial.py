# Generated by Django 3.1.3 on 2020-11-16 14:39

from django.db import migrations, models
import mapbox_location_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('free', models.BooleanField(default=False)),
                ('coordinates', mapbox_location_field.models.LocationField(map_attrs={'center': (35.921637, -79.077887), 'id': 'map', 'navigation_buttons': True, 'rotate': True, 'style': 'mapbox://styles/mapbox/streets-v11', 'track_location_button': True, 'zoom': 5})),
                ('address', mapbox_location_field.models.AddressAutoHiddenField(map_id='map')),
                ('location_type', models.CharField(blank=True, choices=[('PA', 'Dog Park'), ('RE', 'Restaurant'), ('VE', 'Veterinarian'), ('TR', 'Trail'), ('HO', 'House')], default='PA', max_length=2, null=True)),
            ],
        ),
    ]
