from django.contrib import admin
from .models import UserbankAccount, UserAddress
# Register your models here.
admin.site.register(UserbankAccount)
admin.site.register(UserAddress)
