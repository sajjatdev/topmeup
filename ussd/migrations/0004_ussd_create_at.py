# Generated by Django 4.1.7 on 2023-02-17 03:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ussd', '0003_alter_ussd_options_alter_ussd_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ussd',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 2, 17, 3, 43, 23, 539832, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
