# Generated by Django 4.2.4 on 2023-08-18 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bouquets', '0003_bouquet_recommended'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bouquet',
            name='events',
            field=models.ManyToManyField(to='bouquets.event', verbose_name='События'),
        ),
    ]
