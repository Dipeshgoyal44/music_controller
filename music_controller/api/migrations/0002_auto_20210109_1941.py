# Generated by Django 3.1.5 on 2021-01-09 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='guess_can_pause',
            new_name='guest_can_pause',
        ),
    ]
