from django.shortcuts import render
from .models import prac
def index(request):
    a = prac.objects.all()
    return render(request,"index.html",{'a':a})

