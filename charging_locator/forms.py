# charging_locator/forms.py

from django import forms
from .models import ChargingStationReview

class ChargingStationReviewForm(forms.ModelForm):
    class Meta:
        model = ChargingStationReview
        fields = ['rating', 'comment']
        labels = {
            'rating': 'Rating (1-5)',
            'comment': 'Comment'
        }
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4})
        }
