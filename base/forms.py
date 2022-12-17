from django.forms import ModelForm
from .models import Room

# create a form with all the attrs that Room Model have
class RoomForm(ModelForm): 
    class Meta:
        model = Room
        fields = '__all__'