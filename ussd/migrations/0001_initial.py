# Generated by Django 4.1.7 on 2023-02-15 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='USSD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('call_log', models.CharField(max_length=255)),
                ('sponsor_number', models.CharField(max_length=255)),
                ('user_number', models.CharField(max_length=255)),
                ('network', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
            options={
                'verbose_name': 'USSD',
                'verbose_name_plural': 'USSDs',
            },
        ),
    ]