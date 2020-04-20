from django.shortcuts import render
from .models import Project

# Create your views here.
def landing(request):
	projects = Project.objects.all()
	return render(request,'portfolio/landing.html', {'projects':projects})