from django import forms
from .models import Participant

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['child_name', 'address', 'age_group', 'hiv_status', 'date_of_birth', 'schooling_status']
        labels = {
            'child_name': 'Child Name',
            'address': 'Address',
            'age_group': 'Age Group',
            'hiv_status': 'HIV Status',
            'date_of_birth': 'Date of Birth',
            'schooling_status': 'Schooling Status'
        }
        widgets = {
            'child_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'age_group': forms.Select(attrs={'class': 'form-control'}), 
            'hiv_status': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'schooling_status': forms.Select(attrs={'class': 'form-control'}), 
        }
