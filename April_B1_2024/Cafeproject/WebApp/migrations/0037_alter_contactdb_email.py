# Generated by Django 5.0.7 on 2024-10-03 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0036_delete_contactaddressdb_contactdb_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactdb',
            name='Email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
    ]
