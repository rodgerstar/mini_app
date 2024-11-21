import os.path

from django.db import models
import uuid
# Create your models here.
def generate_unique_names(instance, filename):
    name = uuid.uuid4()
    full_file_name = f"{name}-{filename}"
    return os.path.join("profile_pictures", full_file_name)

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    weight = models.IntegerField(default=0)
    profile_pic = models.ImageField(upload_to=generate_unique_names, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'customers'

class Deposit(models.Model):
    amount = models.IntegerField()
    status = models.BooleanField(default=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.customer.first_name} - {self.amount} '

    class Meta:
        db_table = 'deposits'



