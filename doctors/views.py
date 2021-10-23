from django.shortcuts import render, redirect

# Create your views here.
def index(request):
# 	return render(request, "doctors/index.html")

# ทดลองชั่วคราว
	return render(request, "doctors/about.html")

def maps(request):
    return render(request, "doctors/maps.html")

def project_requirement(request):
    return render(request, "doctors/requirement.html")