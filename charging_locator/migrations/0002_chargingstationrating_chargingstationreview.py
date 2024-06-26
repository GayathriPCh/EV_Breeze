# Generated by Django 4.2.5 on 2024-04-11 06:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('charging_locator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChargingStationRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('average_rating', models.DecimalField(decimal_places=2, max_digits=3, null=True)),
                ('charging_station', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='charging_locator.chargingstation')),
            ],
        ),
        migrations.CreateModel(
            name='ChargingStationReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('charging_station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charging_locator.chargingstation')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('charging_station', 'user')},
            },
        ),
    ]
