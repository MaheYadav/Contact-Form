from django import forms
from .models import ContactData
class Contactform(forms.Form):
    first_name=forms.CharField(
        label="Enter Your First Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'First Name'

            }
        )
    )
    last_name = forms.CharField(
        label="Enter Your last Name",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Last Name'

            }
        )
    )
    salary = forms.IntegerField(
        label="Enter Your Salary",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Salary'

            }
        )
    )
    location = forms.CharField(
        label="Enter Your Location",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Location'

            }
        )
    )
    mobile = forms.IntegerField(
        label="Enter Your Number",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Mobile Number'

            }
        )
    )