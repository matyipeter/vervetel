from django import forms
from .models import Patients, DateTimes

class PatientForm(forms.ModelForm):
    date = forms.DateField()
    time= forms.TimeField()

    class Meta:
        model = Patients
        fields = ['first_name', 'last_name', 'email', 'phone_num', 'date', 'time']
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'name':'firstname',
                    'id': 'name',
                    'placeholder':'Kovács',
                    'type':'text'
                }
            ),
            'last_name' : forms.TextInput(
                attrs={
                    'name':'lastname',
                    'id': 'name',
                    'placeholder':'István',
                    'type':'text'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'name': 'email',
                    'type':'email',
                    'id': 'email',
                    'placeholder': 'kovistvan@gmail.com'
                }
            ),
            'phone_num': forms.NumberInput(
                attrs={
                    'name': 'phone',
                    'type':'number',
                    'id': 'phonenum',
                    'placeholder': '305559999'
                }
            ),
        }
        
