# Generated by Django 3.1.3 on 2020-11-22 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_notification_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='message',
        ),
    ]
