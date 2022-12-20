from django.forms import ModelForm
from .models import Room
from django.contrib.auth.models import User

# create a form with all the attrs that Room Model have
class RoomForm(ModelForm): 
    class Meta:
        model = Room
        fields = '__all__'


class UserForm(ModelForm):
    class Meta: 
        model = User
        fields = ['username', 'email']