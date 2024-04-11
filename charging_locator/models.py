# charging_locator/models.py

from django.db import models
from django.contrib.auth.models import User

class ChargingStation(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name

class ChargingStationReview(models.Model):
    charging_station = models.ForeignKey(ChargingStation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['charging_station', 'user']  # Each user can only submit one review per charging station

    def __str__(self):
        return f"Review for {self.charging_station}: {self.rating}"

class ChargingStationRating(models.Model):
    charging_station = models.OneToOneField(ChargingStation, on_delete=models.CASCADE)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2, null=True)

    def update_average_rating(self):
        reviews = ChargingStationReview.objects.filter(charging_station=self.charging_station)
        if reviews.exists():
            total_rating = sum(review.rating for review in reviews)
            self.average_rating = total_rating / reviews.count()
        else:
            self.average_rating = None
        self.save()

    def __str__(self):
        return f"Rating for {self.charging_station}: {self.average_rating}"
