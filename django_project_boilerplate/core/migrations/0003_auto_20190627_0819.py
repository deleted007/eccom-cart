# Generated by Django 2.2 on 2019-06-27 08:19

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20190627_0639'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='item',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.OrderItem'),
        ),
        migrations.AddField(
            model_name='order',
            name='orderd',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='ordered_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 27, 8, 18, 58, 774919, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='recieved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2019, 6, 27, 8, 19, 8, 903183, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='item',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.Item'),
        ),
    ]