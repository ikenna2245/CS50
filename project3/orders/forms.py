from django.forms import ModelForm
from .models import Review

# Create the form class.

class ReviewForm (ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review']
