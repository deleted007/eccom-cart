# Generated by Django 2.2 on 2019-06-27 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190627_0819'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='ordered',
            new_name='orderd',
        ),
    ]