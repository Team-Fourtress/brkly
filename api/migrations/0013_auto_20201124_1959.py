# Generated by Django 3.1.3 on 2020-11-24 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20201123_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='convo_name',
            field=models.CharField(max_length=63),
        ),
    ]
