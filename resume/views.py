from django.shortcuts import render
from django.http import HttpResponse
from resume.models import employment
from resume.models import personal
from resume.models import skills
from resume.models import edu

# Create your views here.
def education(request):
    return render(request,"my_education.html",{})
def home(request):
    return render(request,"home.html",{})
def experience(request):
    return render(request,"my_exp.html",{})
def employment_view(request):
	query_results = employment.objects.all()
	
	context= {'query_results': query_results}

	return render(request,"employment.html",context)

def personal_view(request):
	query_results = personal.objects.all()
	
	context= {'query_results': query_results}

	return render(request,"personal.html",context)