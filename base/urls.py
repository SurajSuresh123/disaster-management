# from django.urls import path
# from . import views

# urlpatterns = [path("", views.home)]
# myapp/urls.py
from django.urls import path
from .views import citizen_register, staff_register,home

urlpatterns = [
    path('',home,name='home-view'),
    path('register/citizen/', citizen_register, name='citizen_register'),
    path('register/staff/', staff_register, name='staff_register'),
    # Add other URLs as needed
]
