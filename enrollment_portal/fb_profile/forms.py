from django import forms
from .models import UserProfile

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic']
        widgets = {
            'profile_pic': forms.FileInput(attrs={
                'id': 'id_profile_pic',
                'accept': 'image/*',
                'class': 'file-input'
            })
        }
