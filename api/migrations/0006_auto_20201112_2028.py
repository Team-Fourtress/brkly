# Generated by Django 3.1.3 on 2020-11-12 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_discussionboard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussionboard',
            name='body',
            field=models.TextField(),
        ),
    ]
