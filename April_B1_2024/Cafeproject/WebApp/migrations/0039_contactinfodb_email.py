# Generated by Django 5.0.7 on 2024-10-04 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0038_contactinfodb_remove_contactdb_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfodb',
            name='Email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]
