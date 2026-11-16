from django.shortcuts import render, redirect
from .forms import *

def index(req):
    if req.method == "POST":
        form = contactform(req.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = contactform()

    return render(req, 'index.html', {'form': form})