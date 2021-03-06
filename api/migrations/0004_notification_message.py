# Generated by Django 3.1.3 on 2020-11-22 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20201122_0219'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='message',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='triggered_notifications', to='api.message'),
            preserve_default=False,
        ),
    ]
