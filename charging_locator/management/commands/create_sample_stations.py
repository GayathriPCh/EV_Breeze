# create_sample_stations.py

from django.core.management.base import BaseCommand
from charging_locator.models import ChargingStation

class Command(BaseCommand):
    help = 'Creates sample charging stations with IDs'

    def handle(self, *args, **kwargs):
        # Define sample charging stations with IDs
        sample_stations = [
            {'id': 1, 'name': 'Station A', 'latitude': 123.456, 'longitude': 789.012},
            {'id': 2, 'name': 'Station B', 'latitude': 456.789, 'longitude': 123.456},
            {'id': 3, 'name': 'Station C', 'latitude': 789.012, 'longitude': 456.789},
        ]

        # Create sample charging stations in the database
        for station_data in sample_stations:
            ChargingStation.objects.update_or_create(id=station_data['id'], defaults={
                'name': station_data['name'],
                'latitude': station_data['latitude'],
                'longitude': station_data['longitude'],
            })

        self.stdout.write(self.style.SUCCESS('Sample charging stations created successfully.'))
