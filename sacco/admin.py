from django.contrib import admin

from sacco.models import Customer, Deposit


# Register your models here.
admin.site.site_header = 'Tujijenge Sacco Administration'


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'gender', 'dob']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['gender']
    list_per_page = 17

class DepositAdmin(admin.ModelAdmin):
    list_display = ['customer', 'created_at', 'status', 'amount']
    search_fields = ['customer', 'created_at', 'status', 'amount']
    list_per_page = 17
    list_filter = ['status']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Deposit, DepositAdmin)







# pyhon manage.py --help