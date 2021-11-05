from django.shortcuts import render, redirect
from doctors.decorator import unauthenticated_user, allowed_users
from doctors.models import *
from .forms import *
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



#ARTICLE

def healthblog(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    print(context)
    return render(request, "doctors/healthblog.html", context)

def healthblog_content(request, pk):
    article = Article.objects.filter(id=pk).first()
    context = {"article": article}
    return render(request, "doctors/healthblog_one.html" ,context)

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
        return redirect("doctors:mhealthblog")


def addArticle(request):
    form = CreateArticleForm()
    if request.method == 'POST':
        createArticleForm = CreateArticleForm(request.POST)
        if createArticleForm.is_valid():
            createArticleForm.save()
            article = Article.objects.values('id').order_by('-id').first()
            id_last = article['id']
            return redirect("doctors:edithealthblog_content", pk=id_last)    #อยากให้ไดเรกไปหน้าที่พึ่ง
    return render(request, "doctors/addhealthblog.html", {"form": form})



#NEW
def news(request):
    news = New.objects.all()
    context = {"news": news}
    return render(request, "doctors/news.html", context)

def news_content(request, pk):
    new = New.objects.filter(id=pk).first()
    context = {"new": new}
    return render(request, "doctors/news_one.html" ,context)

def editnews(request):
    return render(request, "doctors/editnews.html")


def editnews_content(request, pk):
    new = New.objects.filter(id=pk).first()
    context = {"new": new}
    return render(request, "doctors/editnews.html" ,context)


def deleteNews(request, pk):
    new = New.objects.filter(id=pk)
    if request.method == "POST":
        new.delete()
        news = New.objects.all()
        context = {"news": news}
        return redirect("doctors:mnews")


def addNews(request):
    form = CreateNewsForm()
    if request.method == 'POST':
        createNewsForm = CreateNewsForm(request.POST)
        if createNewsForm.is_valid():
            createNewsForm.save()
            news = New.objects.values('id').order_by('-id').first()
            id_last = news['id']
            return redirect("doctors:editnews_content", pk=id_last)    #อยากให้ไดเรกไปหน้าที่พึ่ง
    return render(request, "doctors/addnews.html", {"form": form})
    


#PACKAGE
def mpromotion(request):
    return render(request, "doctors/mpromotion.html")


def editpromotion(request):
    return render(request, "doctors/editpromotion.html")


def mdoctor(request):
    return render(request, "doctors/mdoctor.html")

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



def editprofile(request):
    context = {}
    check = Patient.objects.filter(user__id=request.user.id)
    if len(check)>0:
        data = Patient.objects.get(user__id=request.user.id)
        context["data"]=data
    if request.method=="POST":
        fn = request.POST["fname"]
        ln = request.POST["lname"]
        em = request.POST["email"]

        usr = User.objects.get(id=request.user.id)
        usr.first_name = fn
        usr.last_name = ln
        usr.email = em
        usr.save()


        if "image" in request.FILES:
            img = request.FILES["image"]
            data.profile_pic = img
            data.save()


        context["status"] = "Changes Saved Successfully"
    return render(request,"doctors/editprofile.html" ,context)



def profile(request):
    return render(request, "doctors/profile.html")