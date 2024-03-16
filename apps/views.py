from django.shortcuts import render
from .models import Company


# Create your views here. 
def index(req):
    return render(req, "index.html")
