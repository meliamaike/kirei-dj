from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Service
from django.urls import reverse

def index(request):
    return HttpResponse("Estos son los servicios")

