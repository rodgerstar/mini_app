from django.contrib import admin

from main.models import Book, Student, Transaction, Payment

admin.site.site_header = 'library MIS'
admin.site.site_title = 'Manage Library MIS'

class StudentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'adm_no']
    search_fields = ['name', 'email', 'phone', 'adm_no']
    list_per_page = 30

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'year', 'isbn', 'subject']
    search_fields =['title', 'author', 'year', 'isbn', 'subject']


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['book', 'student', 'expected_return_date']
    search_fields = ['book', 'student', 'expected_return_date']
    list_per_page = 30

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['transaction', 'code', 'status', 'created_at']
    search_fields = ['transaction', 'code', 'status', 'created_at']
    list_per_page = 25

admin.site.register(Student, StudentsAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Payment, PaymentAdmin)