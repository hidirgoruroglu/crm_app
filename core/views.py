from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.
def index(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request,user)
            messages.success(request, "You have been logged in!")
            return redirect("index")
        else:
            messages.warning(request, "There was an error logging in, please try again...")
    
    records = Record.objects.all()

    context = dict(records = records)
    return render(request, "core/index.html", context)

def logout_view(request):
    logout(request)
    messages.warning(request,"You have been logged out!")
    return redirect("index")

def register_view(request):
    if request.user.is_authenticated:
        messages.warning(request, "You already have an account and you are logged in, if you want to create a new account, please log out first.")
        return redirect("index")
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user, backend='django.contrib.auth.backends.ModelBackend')

            messages.success(request, "You have successfully registered!")
            return redirect("index")
    else:

        form = SignUpForm()

        context = dict(form = form)
        return render(request, "core/register.html", context)
    context = dict(form = form)
    return render(request, "core/register.html", context)

def add_record_view(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record added...")
                return redirect("index")
        context = dict(form = form)
        return render(request, "core/add_record.html", context)
    else:
        messages.warning(request, "You must be logged in...")
        return redirect("index")

def customer_record_view(request, id):
    if request.user.is_authenticated:
        customer_record = get_object_or_404(Record, id = id)
        context = dict(customer_record = customer_record)
        return render(request, "core/customer_record.html", context)
    else:
        messages.warning(request, "You must be logged in to view that page")
        return redirect("index")
    
def delete_record_view(request, id):
    if request.user.is_authenticated:
        delete_it = get_object_or_404(Record, id = id)
        delete_it.delete()
        messages.success(request,"The records is deleted!")
        return redirect("index")
    else:
        messages.warning(request, "You must be logged in to do that")
        return redirect("index")

def update_record_view(request, id):
    if request.user.is_authenticated:
        current_record = get_object_or_404(Record, id = id)
        form = AddRecordForm(request.POST or None, instance = current_record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record has been updated!")
            return redirect("index")
        context = dict(form = form)
        return render(request, "core/update_record.html", context)
    else:
        messages.warning(request, "You must be logged in...")
        return redirect("index")
