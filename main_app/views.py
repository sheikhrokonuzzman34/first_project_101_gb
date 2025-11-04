from django.shortcuts import render, redirect
from main_app.models import *

# Create your views here.

def index(request):
    profile_image = Profile.objects.last()
    return render(request, 'main_app/index.html', {'profile_image': profile_image})

def projects(request):
    pro = Project.objects.all()
    return render(request, 'main_app/projects.html', {'pro': pro})

from main_app.forms import ContactMessageForm
def contact(request):
    form = ContactMessageForm()
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ContactMessageForm()
    return render(request, 'main_app/contact.html', {'form': form})



