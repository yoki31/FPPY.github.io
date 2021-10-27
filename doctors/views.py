from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    # context = {}
	return render(request, "doctors/index.html")#, context)

def about(request):
	return render(request, "doctors/about.html")

def maps(request):
    return render(request, "doctors/maps.html")

def project_requirement(request):
    return render(request, "doctors/requirement.html")

def healthblog(request):
    return render(request, "doctors/healthblog.html")
    
def healthblog_one(request):
    return render(request, "doctors/healthblog_one.html")

def news(request):
    return render(request, "doctors/news.html")
    
def news_one(request):
    return render(request, "doctors/news_one.html")

# user
def userhome(request):
    return render(request, "doctors/userhome.html")

def uhealthblog(request):
    return render(request, "doctors/uhealthblog.html")
    
def uhealthblog_one(request):
    return render(request, "doctors/uhealthblog_one.html")

def unews(request):
    return render(request, "doctors/unews.html")
    
def unews_one(request):
    return render(request, "doctors/unews_one.html")

# admin
def mhealthblog(request):
    return render(request, "doctors/mhealthblog.html")

def mnews(request):
    return render(request, "doctors/mnews.html")

def mdoctor(request):
    return render(request, "doctors/mdoctor.html")

# มันต้องแตกตามหน้าย่อย ต้องส่งหัวข้อ รูป เนื้อหาเข้าไป จำไม่ได้ ฝากทำหน่อย
def edithealthblog(request):
    return render(request, "doctors/edithealthblog.html")
    
def editnews(request):
    return render(request, "doctors/editnews.html")