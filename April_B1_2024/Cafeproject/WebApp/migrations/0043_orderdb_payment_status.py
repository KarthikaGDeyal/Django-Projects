# Generated by Django 5.0.7 on 2024-10-08 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0042_footerdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdb',
            name='payment_status',
            field=models.CharField(default='Pending', max_length=20),
        ),
    ]
