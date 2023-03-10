from app4.views import *
from django.urls import path
app_name='nothing'
urlpatterns=[
    path('adrenaline/',adrenaline,name='adrenaline'),
]