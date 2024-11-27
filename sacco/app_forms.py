from django import forms
from sacco.models import Customer, Deposit

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

class CustomerForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'dob', 'weight', 'gender', 'profile_pic']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date', 'min': '1980-01-01', 'max': '2023-12-31', 'autocomplete': 'bday'}),  # 'bday' for date of birth
            'weight': forms.NumberInput(attrs={'type': 'number', 'min': '10', 'max': '1000', 'autocomplete': 'off'}),  # 'off' for fields that should not autofill
            'gender': forms.Select(choices=GENDER_CHOICES, attrs={'autocomplete': 'sex'}),  # 'sex' is a valid value for gender
            'first_name': forms.TextInput(attrs={'autocomplete': 'given-name'}),  # 'given-name' for first name
            'last_name': forms.TextInput(attrs={'autocomplete': 'family-name'}),  # 'family-name' for last name
            'email': forms.EmailInput(attrs={'autocomplete': 'email'}),  # 'email' for email field
        }

class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = ['amount']
        widgets = {
            'amount': forms.NumberInput(attrs={'type': 'number', 'min': '10', 'max': '1000000', 'autocomplete': 'off'}),  # 'off' for non-sensitive fields
        }

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'autocomplete': 'username'}))  # 'username' for username field
    password = forms.CharField(widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}))  # 'current-password' for password field
