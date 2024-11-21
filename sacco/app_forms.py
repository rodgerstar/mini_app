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
            'dob' : forms.DateInput(attrs={'type':'date', 'min':'1980-01-01', 'max':'2023-12-31'}),
            'weight' : forms.NumberInput(attrs={'type':'number', 'min':'10', 'max':'1000'}),
            'gender': forms.Select(choices=GENDER_CHOICES),
        }

class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = ['amount']

        widgets = {
            'amount' : forms.NumberInput(attrs={'type':'number', 'min':'10', 'max':'1000000'}),
        }
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)