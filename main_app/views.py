from django.shortcuts import render
from main_app.models import *

# Create your views here.

def index(request):
    profile_image = Profile.objects.last()
    return render(request, 'main_app/index.html', {'profile_image': profile_image})

def projects(request):
    pro = Project.objects.all()
    return render(request, 'main_app/projects.html', {'pro': pro})



