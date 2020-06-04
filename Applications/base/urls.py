from django.urls import path
from .views import *

urlpatterns = [
    path('', Main.as_view(), name = 'index'),
    path('main/',GlobalListing.as_view(), {'categoryName' : 'Main'}, name='main'),
    path('programing/',GlobalListing.as_view(), {'categoryName' : 'Programing'}, name='programing'),
    path('contact/', ContactForm.as_view(), name = 'contact')
]