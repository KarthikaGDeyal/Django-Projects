# Generated by Django 5.0.7 on 2024-09-29 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0015_checkoutdb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='checkoutdb',
            old_name='FirstName',
            new_name='Username',
        ),
        migrations.RemoveField(
            model_name='checkoutdb',
            name='LastName',
        ),
    ]
