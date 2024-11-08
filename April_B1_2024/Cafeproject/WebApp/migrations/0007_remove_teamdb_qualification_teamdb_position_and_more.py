# Generated by Django 5.0.7 on 2024-09-26 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0006_teamdb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teamdb',
            name='Qualification',
        ),
        migrations.AddField(
            model_name='teamdb',
            name='Position',
            field=models.CharField(blank=True, choices=[('PastryChef', 'PastryChef'), ('Decorator', 'Decorator'), ('Assistant', 'Assistant'), ('Recipe Developer', 'Recipe Developer'), ('Kitchen Porter', 'Kitchen Porter'), ('Head Baker', 'Head Baker')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='teamdb',
            name='ProfileImage',
            field=models.FileField(blank=True, null=True, upload_to='profile/'),
        ),
    ]
