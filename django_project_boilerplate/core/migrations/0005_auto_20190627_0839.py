# Generated by Django 2.2 on 2019-06-27 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190627_0826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='orderd',
            new_name='ordered',
        ),
        migrations.RenameField(
            model_name='orderitem',
            old_name='orderd',
            new_name='ordered',
        ),
    ]