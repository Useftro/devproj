from django.forms import ModelForm
from mapapp.models import Point


class PointForm(ModelForm):
    class Meta:
        model = Point
        fields = ['lat', 'lng']
