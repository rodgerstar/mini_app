from django.http import HttpResponse
from django.shortcuts import render, redirect

from sacco.models import Customer, Deposit


# Create your views here.
# def test(request):

    # c1 = Customer(first_name='John', last_name='Smith',email='joea@gmail.com',
    #               dob='2000-11-21', gender='male', weight=45)
    #
    # c1.save()
    #
    # c2 = Customer(first_name='ohn', last_name='mit', email='joemita@gmail.com',
    #               dob='2000-11-21', gender='female', weight=55)
    #
    # c2.save()

    # customer_count = Customer.objects.count()
    #
    # c1 = Customer.objects.get(id=1)
    # print(c1)
    #
    # d1 = Deposit(amount=1000, status=True, customer=c1)
    # d1.save()
    #
    # deposit_count = Deposit.objects.count()
    #
    # return HttpResponse(f"OK, Done, we have {customer_count} customers and {deposit_count} deposits")
def customers(request):
    customers_data = Customer.objects.all()

    return render(request, 'customers.html', {'Customers':customers_data})


def delete_customer(request, customer_id):
    customers_data = Customer.objects.get(id=customer_id)
    customers_data.delete()
    return redirect('customers')

  # Check if all IDs are populated

