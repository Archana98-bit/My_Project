# Generated by Django 5.0.2 on 2024-04-30 20:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OdishaTourismApp', '0002_tourismmodel_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='CultureModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FestivalName', models.CharField(max_length=25)),
                ('YourName', models.CharField(max_length=25)),
                ('FestivalDetails', models.CharField(max_length=255)),
                ('City', models.CharField(max_length=25)),
                ('State', models.CharField(max_length=25)),
                ('Image', models.ImageField(upload_to='Images/')),
                ('Date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='TourismModel',
        ),
    ]
