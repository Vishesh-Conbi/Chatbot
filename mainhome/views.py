from django.shortcuts import render,redirect
from .models import content,demo_book
from django.contrib import messages
from pathlib import Path
import os

# Create your views here.
def chatscreen(request):

    if request.method == "POST":
        pass

    


       
    else:
        cont = content.objects.all()
        return render(request,"chatscreen.html" , {'cont':cont})
