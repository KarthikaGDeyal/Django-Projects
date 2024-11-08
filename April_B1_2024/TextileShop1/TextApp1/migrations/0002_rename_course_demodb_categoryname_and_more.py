# Generated by Django 5.0.7 on 2024-07-21 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TextApp1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='demodb',
            old_name='Course',
            new_name='CategoryName',
        ),
        migrations.RenameField(
            model_name='demodb',
            old_name='Address',
            new_name='Description',
        ),
        migrations.RemoveField(
            model_name='demodb',
            name='Age',
        ),
        migrations.RemoveField(
            model_name='demodb',
            name='Email',
        ),
        migrations.RemoveField(
            model_name='demodb',
            name='Gender',
        ),
        migrations.RemoveField(
            model_name='demodb',
            name='Mobile',
        ),
        migrations.RemoveField(
            model_name='demodb',
            name='Name',
        ),
        migrations.AddField(
            model_name='demodb',
            name='CategoryImage',
            field=models.ImageField(blank=True, null=True, upload_to='Category_Pictures'),
        ),
    ]
