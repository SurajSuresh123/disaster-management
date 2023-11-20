# from django.shortcuts import render
# from django.http import HttpResponse

# def home(request):
#   return HttpResponse("hello world")

# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CitizenUserCreationForm, StaffUserCreationForm

def home(request):
    return render(request,'home.html',{})
def citizen_register(request):
    if request.method == 'POST':
        form = CitizenUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page or another URL
    else:
        form = CitizenUserCreationForm()
    return render(request, 'registration/citizen_register.html', {'form': form})

def staff_register(request):
    if request.method == 'POST':
        form = StaffUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page or another URL
    else:
        form = StaffUserCreationForm()
    return render(request, 'registration/staff_register.html', {'form': form})
