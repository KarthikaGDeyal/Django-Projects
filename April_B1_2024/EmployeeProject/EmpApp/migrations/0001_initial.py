# Generated by Django 5.0.7 on 2024-07-16 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=50, null=True)),
                ('Email', models.CharField(blank=True, max_length=50, null=True)),
                ('Mobile', models.IntegerField(blank=True, null=True)),
                ('Salary', models.IntegerField(blank=True, null=True)),
                ('Location', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
