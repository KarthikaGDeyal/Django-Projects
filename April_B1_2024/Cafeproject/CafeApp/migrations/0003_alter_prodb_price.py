# Generated by Django 5.0.7 on 2024-08-17 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CafeApp', '0002_prodb_productimage3_prodb_productimage4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prodb',
            name='Price',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
