# Generated by Django 5.0.7 on 2024-10-01 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0029_alter_cartdb_total_price_alter_orderdb_total_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassListDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='class_images/')),
                ('additional_info', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
