# Generated by Django 5.0.7 on 2024-09-30 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0026_alter_wishlistdb_stock'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wishlistdb',
            old_name='Product_name',
            new_name='ProductName',
        ),
    ]
