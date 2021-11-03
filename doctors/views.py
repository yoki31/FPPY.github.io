from django.shortcuts import render, redirect
from doctors.decorator import unauthenticated_user, allowed_users
from doctors.models import *
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
# Create your views here.


def index(request):
    # context = {}
    return render(request, "doctors/index.html")  # , context)


def about(request):
    return render(request, "doctors/about.html")


def maps(request):
    return render(request, "doctors/maps.html")


def project_requirement(request):
    return render(request, "doctors/requirement.html")


def healthblog(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    print(context)
    return render(request, "doctors/healthblog.html", context)


def healthblog_one(request):
    # article = Article.objects.filter(id=pk)
    # context = {"article": article}
    # print(context)
    return render(request, "doctors/healthblog_one.html")


def healthblog_content(request, pk):
    article = Article.objects.filter(id=pk).first()
    context = {"article": article}
    return render(request, "doctors/healthblog_one.html" ,context)


def news(request):
    news = News.objects.all()
    context = {"news": news}
    return render(request, "doctors/news.html", context)


def news_one(request):
    return render(request, "doctors/news_one.html")


def news_content(request, pk):
    new = News.objects.filter(id=pk).first()
    context = {"new": new}
    return render(request, "doctors/news_one.html" ,context)

# user


def userhome(request):
    return render(request, "doctors/userhome.html")


def umaps(request):
    return render(request, "doctors/umaps.html")


def uhealthblog(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "doctors/uhealthblog.html", context)


def uhealthblog_one(request):
    return render(request, "doctors/uhealthblog_one.html")


def uhealthblog_content(request, pk):
    article = Article.objects.filter(id=pk).first()
    context = {"article": article}
    return render(request, "doctors/uhealthblog_one.html" ,context)


def unews(request):
    news = News.objects.all()
    context = {"news": news}
    return render(request, "doctors/unews.html", context)


def unews_one(request):
    return render(request, "doctors/unews_one.html")


def unews_content(request, pk):
    new = News.objects.filter(id=pk).first()
    context = {"new": new}
    return render(request, "doctors/unews_one.html" ,context)

def udpromotion(request):
    return render(request, "doctors/udpromotion.html")

# admin


def adminhome(request):
    return render(request, "doctors/adminhome.html")


def mhealthblog(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "doctors/mhealthblog.html", context)


def edithealthblog(request):
    return render(request, "doctors/edithealthblog.html")


def edithealthblog_content(request, pk):
    article = Article.objects.filter(id=pk).first()
    context = {"article": article}
    return render(request, "doctors/edithealthblog.html" ,context)
    
    
def deleteArticle(request, pk):
    article = Article.objects.filter(id=pk)
    if request.method == "POST":
        article.delete()
        articles = Article.objects.all()
        context = {"articles": articles}
        return redirect("doctors:mhealthblog")
    

def mnews(request):
    news = News.objects.all()
    context = {"news": news}
    return render(request, "doctors/mnews.html", context)


def editnews(request):
    return render(request, "doctors/editnews.html")


def editnews_content(request, pk):
    new = News.objects.filter(id=pk).first()
    context = {"new": new}
    return render(request, "doctors/editnews.html" ,context)


def deleteNews(request, pk):
    new = News.objects.filter(id=pk)
    if request.method == "POST":
        new.delete()
        news = News.objects.all()
        context = {"news": news}
        return redirect("doctors:mnews")


def mdoctor(request):
    return render(request, "doctors/mdoctor.html")


def mpromotion(request):
    return render(request, "doctors/mpromotion.html")


def dpromotion(request):
    return render(request, "doctors/dpromotion.html")

# มันต้องแตกตามหน้าย่อย ต้องส่งหัวข้อ รูป เนื้อหาเข้าไป จำไม่ได้ ฝากทำหน่อย
#หมายถึงลบ เพิ่ม แก้ไขหรอวะ

# def edithealthblog(request, pk):
#     article = Article.objects.filter(id=pk).first()
#     context = {"article": article}
#     return render(request, "doctors/edithealthblog.html" ,context)


# def editnews(request):
#     return render(request, "doctors/editnews.html")


#register / login / logout

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='Patient')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)
            return redirect('doctors:login')
    return render(request, 'doctors/register.html', {'form': form})

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('doctors:index')
        else:
            messages.info(request, 'Username or Password is invalid')
    return render(request, 'doctors/login.html')


def logoutPLS(request):
    logout(request)
    return redirect('doctors:login')

# @login_required(login_url='doctors:login') อยากให้ login ตรงไหนก็เอาไปใส่ช้างบน def นะ
# @allowed_users(allowed_roles=['xxxxx'])   กลุ่มของบท

def mcustomer(request):
    return render(request, "doctors/mcustomer.html")

def editpromotion(request):
    return render(request, "doctors/editpromotion.html")