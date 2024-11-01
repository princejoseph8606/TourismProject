from django import forms
from django.contrib.auth.models import User
from .models import TravelPackage

class VendorSignupForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class UserSignupForm(VendorSignupForm):  # Extends VendorSignupForm
    pass

class VendorLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class TravelPackageForm(forms.ModelForm):
    class Meta:
        model = TravelPackage
        fields = [
            'package_name', 'max_number_of_persons', 'hotel_type',
            'food_type', 'number_of_days', 'number_of_nights',
            'visiting_places', 'description', 'tour_date',
            'image1', 'image2', 'image3'
        ]
        widgets = {
            'tour_date': forms.DateInput(attrs={'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['package_name'].required = False  # Make 'package_name' optional in the form
        self.fields['tour_date'].required = False
