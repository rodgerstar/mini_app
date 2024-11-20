from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from pyexpat.errors import messages

from sacco.app_forms import CustomerForm, DepositForm, LoginForm
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
@login_required
def customers(request):
    data = Customer.objects.all().order_by('-id').values()
    paginator = Paginator(data, 15)
    page_number = request.GET.get('page', 1)
    try:
        paginated_data = paginator.page(page_number)
    except PageNotAnInteger:
        paginated_data = paginator.page(1)

    return render(request, 'customers.html', {'data':paginated_data})

@login_required
def delete_customer(request, customer_id):
    customers_data = Customer.objects.get(id=customer_id)
    customers_data.delete()
    return redirect('customers')

  # Check if all IDs are populated
@login_required
def customer_detail(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    deposits = Deposit.objects.filter(customer_id=customer_id)
    return render(request, "details.html", {"deposits": deposits, "customer": customer})

@login_required
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers')
    else:
        form = CustomerForm()
    return render(request, 'customer_form.html' , {'form': form})

@login_required
def update_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers')  # Redirect to the customers list after saving
    else:
        form = CustomerForm(instance=customer)  # Pre-fill form with customer data for GET request

    # Pass customer_id to the template context
    return render(request, 'customer_update_form.html', {'form': form, 'customer_id': customer_id})

@login_required
def search_customer(request):
    search_term = request.GET.get('search', '')  # Default to an empty string if no search term
    data = Customer.objects.filter(
        Q(first_name__icontains=search_term) |
        Q(last_name__icontains=search_term) |
        Q(email__icontains=search_term)
    ).order_by('-id')  # Add order to results for consistency

    paginator = Paginator(data, 15)  # Paginate the search results
    page_number = request.GET.get('page', 1)

    try:
        paginated_data = paginator.page(page_number)
    except PageNotAnInteger:
        paginated_data = paginator.page(1)
    except EmptyPage:
        paginated_data = paginator.page(paginator.num_pages)

    return render(request, 'search.html', {'data': paginated_data, 'search_term': search_term})

@login_required
def deposit(request, customer_id):
    # Fetch the customer or return a 404 error if not found
    customer = get_object_or_404(Customer, id=customer_id)

    if request.method == 'POST':
        form = DepositForm(request.POST)  # Bind the submitted data to the form
        if form.is_valid():
            deposit = form.save(commit=False)  # Save the deposit instance but don’t commit yet
            deposit.customer = customer  # Associate the deposit with the fetched customer
            deposit.save()  # Save to the database
            return redirect('customers')  # Redirect to the customer's detail page
    else:
        form = DepositForm()  # Instantiate an empty form for a GET request

    # Render the deposit form with the customer context
    return render(request, 'deposit_form.html', {'form': form, 'customer': customer})


def login_user(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login_form.html', {"form": form} )
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user :
                login(request, user)
                return redirect('customers')
        # messages.error(request, 'Invalid username or password.')
        return render(request, 'login_form.html', {"form": form})
@login_required
def signout_user(request):
    logout(request)
    return redirect('login')