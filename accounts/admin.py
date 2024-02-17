from django.contrib import admin
from .models import UserBankAccount, userAddress
# Register your models here.

admin.site.register(UserBankAccount)
admin.site.register(userAddress)

