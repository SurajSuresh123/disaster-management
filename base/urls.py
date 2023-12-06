# from django.urls import path
# from . import views

# urlpatterns = [path("", views.home)]
# myapp/urls.py
from django.urls import path
from .views import citizen_register, staff_register,home,citizen_login,staff_login,citizen_applicationform,citizen_details_display,citizen_application_status,staff_home,displaytostaff,surveyform_fill,display_surveyform,citizen_home

urlpatterns = [
    path('',home,name='home-view'),
    path('register/citizen/', citizen_register, name='citizen_register'),
    path('register/staff/', staff_register, name='staff_register'),
    path('login/citizen/',citizen_login,name='citizen_login'),
    path('login/staff/',staff_login,name='staff_login'),
    path('citizen/home/',citizen_home,name='citizen-home'),
    path('citizen/applicationform/',citizen_applicationform,name='citizen_applicationform'),
    path('citizen/applicationform_display',citizen_details_display,name='citizen-details-display'),
    path('citizen/application_status',citizen_application_status,name='app-status'),
    path('staff/home/',staff_home,name='staff-home'),
    path('staff/home/<str:username>',displaytostaff,name='each-citizen'),
    path('staff/home/survey/<str:username>',surveyform_fill,name='fill-survey'),
    path('staff/home/survey_display/<str:username>',surveyform_fill,name='display-survey')
    # Add other URLs as needed
]
