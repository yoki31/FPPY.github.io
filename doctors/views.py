from django.shortcuts import render, redirect

# Create your views here.
def index(request):
	return render(request, "doctors/index.html")

def about(request):
	return render(request, "doctors/about.html")

def maps(request):
    return render(request, "doctors/maps.html")

def project_requirement(request):
    return render(request, "doctors/requirement.html")

def healthblog(request):
    return render(request, "doctors/healthblog.html")

def news(request):
    return render(request, "doctors/news.html")

# user
def userhome(request):
    return render(request, "doctors/userhome.html")

def uhealthblog(request):
    return render(request, "doctors/uhealthblog.html")

def unews(request):
    return render(request, "doctors/unews.html")

# admin
def mhealthblog(request):
    return render(request, "doctors/mhealthblog.html")

def mnews(request):
    return render(request, "doctors/mnews.html")