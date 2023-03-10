from django.shortcuts import render
from django.http import HttpResponse
def ghrelin(request):
    return HttpResponse('ghrelin is a hormone which releases at the time of hungry ')

# Create your views here.
