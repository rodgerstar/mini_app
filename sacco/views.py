from django.core.paginator import Paginator, PageNotAnInteger
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
    customers_data = Customer.objects.all().order_by('id').values()
    paginator = Paginator(customers_data, 15)
    page_number = request.GET.get('page', 1)
    try:
        paginated_data = paginator.page(page_number)
    except PageNotAnInteger:
        paginated_data = paginator.page(1)

    return render(request, 'customers.html', {'data':paginated_data})


def delete_customer(request, customer_id):
    customers_data = Customer.objects.get(id=customer_id)
    customers_data.delete()
    return redirect('customers')

  # Check if all IDs are populated

def customer_detail(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    deposits = Deposit.objects.filter(customer_id=customer_id)
    return render(request, "details.html", {"deposits": deposits, "customer": customer})
