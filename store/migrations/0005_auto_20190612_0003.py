# Generated by Django 2.2.1 on 2019-06-12 04:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20190611_1038'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='order',
            name='status_date',
            field=models.DateField(default=datetime.date(2019, 6, 12)),
        ),
    ]
