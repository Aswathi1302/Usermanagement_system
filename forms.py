from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['No', 'first_name','last_name','DOB','address']
        labels={
            'No':'No',
            'first_name':'first_name',
            'last_name':'last_name',
            'DOB':'DOB',
            'address':'address'


        }
        widgets={
            'No':forms.NumberInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'DOB':forms.TextInput(attrs={'class': 'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'})


        }
