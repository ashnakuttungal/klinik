from django.contrib import admin
from django.urls import path,include 
from. import views

urlpatterns = [
path('index2',views.index2),
path('doctoruserviews',views.doctoruserviews),
path('doctorbooking',views.doctorbooking),
path('userprofile',views.userprofile),
path('appointment_view',views.appointment_view),
path('appointment_delete/<int:id>',views.appointment_delete,name="appointment_delete"),
path('appointment_update/<int:id>',views.appointment_update,name="appointment_update"),
path('appointment_update/appointments_update/<int:id>',views.appointments_update,name="appointments_update"),
]