from app3.views import *
from django.urls import path
app_name='something'
urlpatterns=[
    path('ghrelin/',ghrelin,name='ghrelin'),
]