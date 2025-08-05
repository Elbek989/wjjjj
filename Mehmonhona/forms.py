from django import forms
from .models import  Room,Deal,User


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['title', 'price']

class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ['start_time','end_time']


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name','p[fone']

