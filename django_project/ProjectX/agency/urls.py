from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),

    path('contact/',views.contact),

    path('properties/',views.properties),

    path('property_details/',views.property_details),

   
]
