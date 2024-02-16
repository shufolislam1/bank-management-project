from django.db import models
from django.contrib.auth.models import User


ACCOUNT_TYPE=(
    ('Savings', 'Savings'),
    ()
)
GENDER_TYPE=(
    ('Male', 'Male'),
    ('Female', 'Female')
)
# Create your models here.
class UserBankAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete= models.CASCADE)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPE)
    account_no = models.IntegerField(unique=True)
    birth_date = models.DateTimeField(null =True, blank=True)
    gender = models.CharField(max_length=20, choices=GENDER_TYPE)
    initial_deposite_date = models.DateField(auto_now_add = True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    