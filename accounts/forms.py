from django.contrib.auth.forms import UserCreationForm
from django import forms
from .constant import ACCOUNT_TYPE, GENDER_TYPE
from django.contrib.auth.models import User
from .models import UserBankAccount, userAddress

class UserRegistrationForm(UserCreationForm):
    birth_date = forms.DateTimeField(null =True, blank=True)
    gender = forms.CharField(max_length=20, choices=GENDER_TYPE)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    postal_code = forms.IntegerField()
    country = forms.CharField(max_length = 100)
    
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'account_type', 'birth_date' 'gender', 'street_address', 'city', 'postal_code', 'country']
        
    def save(self, commit = True):
        our_user = super().save(commit=False)
        if commit == True:
            our_user.save()
            account_type = self.cleaned_data.get('account_type')
            birth_date = self.cleaned_data.get('birth_date')
            gender = self.cleaned_data.get('gender')
            
            street_address = self.cleaned_data.get('street_address')
            city = self.cleaned_data.get('city')
            postal_code = self.cleaned_data.get('postal_code')
            country = self.cleaned_data.get('country')
            
            userAddress.objects.create(
                user = our_user,
                street_address= street_address,
                city = city,
                postal_code = postal_code,
                country = country
            )
            
            UserBankAccount.objects.create(
                User = our_user,
                account_type= account_type,
                birth_date = birth_date,
                gender = gender
            )
            
            
        