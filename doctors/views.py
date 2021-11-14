from django.shortcuts import render, redirect
from doctors.decorator import *
from doctors.models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
import os
from django.contrib import messages
from django.db.models import Q
from datetime import date, datetime
# from django.contrib.admin.widgets import  AdminDateWidget
# Create your views here.


def index(request):
    articles = Article.objects.all()
    news = New.objects.all()
    return render(request, "doctors/index.html", {"articles": articles, "news": news})

def about(request):
    return render(request, "doctors/about.html")

def maps(request):
    return render(request, "doctors/maps.html")

def project_requirement(request):
    return render(request, "doctors/requirement.html")

#-----------------------------------------------------------------------------------

# ARTICLE

def healthblog(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "doctors/healthblog.html", context)

def healthblog_content(request, pk):
    article = Article.objects.filter(id=pk).first()
    context = {"article": article}
    return render(request, "doctors/healthblog_one.html", context)

@admin_only
def deleteArticle(request, pk):
    article = Article.objects.get(id=pk)
    if request.method == "POST":
        article.delete()
        return redirect("doctors:healthblog")

@admin_only
def addArticle(request):
    form = CreateArticleForm()
    if request.method == 'POST':
        form = CreateArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            article = Article.objects.values('id').order_by('-id').first()
            id_last = article['id']
            # อยากให้ไดเรกไปหน้าที่พึ่ง
            return redirect("doctors:healthblog_content", pk=id_last)
    return render(request, "doctors/addhealthblog.html", {"form": form})

@admin_only
def updateArticle(request, pk):
    article = Article.objects.get(id=pk)
    form = CreateArticleForm(instance=article)
    if request.method == 'POST':
        createNewsForm = CreateArticleForm(
            request.POST, request.FILES, instance=article)
        if createNewsForm.is_valid():
            createNewsForm.save()
            article = Article.objects.values('id').order_by('-id').first()
            id_last = article['id']
            return redirect("doctors:healthblog_content", pk=id_last)
    context = {"form": form, "article": article}
    return render(request, "doctors/updatehealthblog.html", context)

#-----------------------------------------------------------------------------------

# NEW
def news(request):
    news = New.objects.all()
    context = {"news": news}
    return render(request, "doctors/news.html", context)

def news_content(request, pk):
    new = New.objects.filter(id=pk).first()
    context = {"new": new}
    return render(request, "doctors/news_one.html", context)

@admin_only
def deleteNews(request, pk):
    new = New.objects.get(id=pk)
    if request.method == "POST":
        new.delete()
        return redirect("doctors:news")

@admin_only
def addNews(request):
    form = CreateNewsForm()
    if request.method == 'POST':
        createNewsForm = CreateNewsForm(request.POST, request.FILES)
        if createNewsForm.is_valid():
            createNewsForm.save()
            news = New.objects.values('id').order_by('-id').first()
            id_last = news['id']
            # อยากให้ไดเรกไปหน้าที่พึ่ง
            return redirect("doctors:news_content", pk=id_last)
    return render(request, "doctors/addnews.html", {"form": form})

@admin_only
def updateNew(request, pk):
    new = New.objects.get(id=pk)
    form = CreateNewsForm(instance=new)
    if request.method == 'POST':
        form = CreateNewsForm(request.POST, request.FILES, instance=new)
        if form.is_valid():
            form.save()
            new = New.objects.values('id').order_by('-id').first()
            id_last = new['id']
            return redirect("doctors:news_content", pk=id_last)
    context = {"form": form, "new": new}
    return render(request, "doctors/updatenews.html", context)

#-----------------------------------------------------------------------------------

# PACKAGE


def package(request):
    packages = Package.objects.all()
    return render(request, "doctors/package.html", {"packages": packages})

def package_content(request, pk):
    pack = Package.objects.filter(id=pk).first()
    return render(request, "doctors/package_one.html", {'pack': pack})

@admin_only
def editpackage(request, pk):
    pack = Package.objects.get(id=pk)
    form = CreatePackageForm(instance=pack)
    if request.method == 'POST':
        form = CreatePackageForm(request.POST, request.FILES, instance=pack)
        if form.is_valid():
            form.save()
            new = Package.objects.values('id').order_by('-id').first()
            id_last = new['id']
            return redirect("doctors:package_content", pk=id_last)
    context = {"form": form}
    return render(request, "doctors/editpackage.html", context)

@admin_only
def deletePackage(request, pk):
    pack = Package.objects.get(id=pk)
    pack.delete()
    return redirect("doctors:package")

@admin_only
def addPackage(request):
    form = CreatePackageForm()
    if request.method == 'POST':
        newform = CreatePackageForm(request.POST, request.FILES)
        if newform.is_valid():
            newform.save()
            pack = Package.objects.values('id').order_by('-id').first()
            id_last = pack['id']
            return redirect("doctors:package_content", pk=id_last)
    return render(request, "doctors/addpackage.html", {"form": form})

@login_required(login_url='doctors:login')
def buy(request , pk):
    pack = Package.objects.get(id=pk)
    pat = request.user.patient
    Buy.objects.create(patient=pat, package=pack)
    return redirect("doctors:package")

@admin_only
def packbuy(request):
    buy = Buy.objects.all()
    return render(request, "doctors/packbuy.html", {'buy': buy})


def mypack(request):
    patient = request.user.patient.buy_set.all()
    return render(request, "doctors/mypack.html", {'patient': patient})

@admin_only
def packbuy_one(request, pk):
    buy = Buy.objects.filter(id=pk).first()
    return render(request, "doctors/packbuy_one.html", {'buy': buy} )

@admin_only
def checkslip(request, pk):
    buy = Buy.objects.get(id=pk)
    form = StatusBuy(instance=buy)
    if request.method == 'POST':
        form = StatusBuy(request.POST, request.FILES, instance=buy)
        if form.is_valid():
            form.save()
        return redirect("doctors:packbuy")    
    return render(request, "doctors/checkslip.html", {"form": form})

def mypack_one(request, pk):
    mypack = request.user.patient.buy_set.get(id=pk)
    return render(request, "doctors/mypack_one.html", {'mypack': mypack})

def sendslip(request, pk):
    mypack = request.user.patient.buy_set.get(id=pk)
    form = SendSlip(instance=mypack)
    if request.method == 'POST':
        form = SendSlip(request.POST, request.FILES, instance=mypack)
        if form.is_valid():
            form.save()
            return redirect("doctors:mypack")
    return render(request, "doctors/sendslip.html", {"form": form})   

#-----------------------------------------------------------------------------------

# Appointment profile

def appointment(request, pk):
    doctor = Doctor.objects.filter(id=pk).first()
    form = AppointmentForm()
    date_now = datetime.now()
    if request.method == 'POST':
        symptom_input = request.POST.get("symptom")
        date_input = request.POST.get("date_input")
        if datetime(int(date_input[:4]), int(date_input[5:7]), int(date_input[8:]),) <= date_now:
            messages.add_message(request, messages.SUCCESS, f"ไม่สามารถนัดพบแพทย์ได้ กรุณาเลือกวันให้ถูกต้อง")   #กรณีนัดวันที่ผ่านมาแล้ว
            return redirect("doctors:appointment", pk)
        appointment = Appointment.objects.create(
            Patient_id=request.user.patient,
            Doctor_id=doctor,
            symptom=symptom_input
        )
        appointment.dateapp = date_input
        appointment.save()
        return redirect("doctors:profile")

    context = {"form": form, "doctor": doctor}
    return render(request, "doctors/appointment_patient.html", context)

# @admin_only    
def deleteAppointment(request, pk):
    appointment = Appointment.objects.get(id=pk)
    appointment.delete()
    return redirect("doctors:profile")

@admin_only
def adminAppointment(request):
    appointment = Appointment.objects.all()
    return render(request, "doctors/mappointment.html", {"appointment": appointment})

def profile(request):
    appointment = Appointment.objects.filter(Patient_id=request.user.patient)
    return render(request, "doctors/profile.html", {"appointment": appointment})

#-----------------------------------------------------------------------------------

#register / login / logout

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='patient')
            user.groups.add(group)
            Patient.objects.create(
                user=user
            )

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

@login_required(login_url='doctors:login')
def account(request):
    patient = request.user.patient
    form = accForm(instance=patient)

    if request.method == 'POST':
        form = accForm(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            form.save()

    return render(request, 'doctors/acc.html', {'form': form})

#-----------------------------------------------------------------------------------

# Doctor
def docprofile(request, pk):
    doctor = Doctor.objects.filter(id=pk).first()
    return render(request, "doctors/docprofile.html", {"doctor": doctor})

@admin_only
def deleteDoc(request, pk):
    doc = Doctor.objects.get(id=pk)
    if request.method == "POST":
        doc.delete()
        return redirect("doctors:spec")

@admin_only
def updateDoc(request, pk):
    doctor = Doctor.objects.get(id=pk)
    form = CreateDocForm(instance=doctor)
    if request.method == 'POST':
        createDocForm = CreateDocForm(
            request.POST, request.FILES, instance=doctor)
        if createDocForm.is_valid():
            createDocForm.save()
            doc = Doctor.objects.values('id').order_by('-id').first()
            id_last = doc['id']
            return redirect("doctors:docprofile" , pk=id_last)
    context = {"form": form, "doctor": doctor}
    return render(request, "doctors/updateDoc.html", context)

def doctor(request):
    return render(request, "doctors/doctor.html")

def finddoc(request):
    if 'q' in request.GET:
        q = request.GET['q']
        mulq = Q(Q(First_name__icontains=q) | Q(Last_name__icontains=q))
        doctors = Doctor.objects.filter(mulq)
    else:
        doctors = Doctor.objects.all()
    context = {'doctors': doctors}
    return render(request, "doctors/finddoc.html", context)

def spec(request):
    list1 = Doctor.objects.filter(spec='อายุรศาสตร์ทั่วไป')
    list2 = Doctor.objects.filter(spec='ศัลยแพทย์ออร์โธปิดิกส์')
    list3 = Doctor.objects.filter(spec='จักษุแพทย์')
    list4 = Doctor.objects.filter(spec='จิตแพทย์')
    list5 = Doctor.objects.filter(spec='สูตินรีแพทย์')
    list6 = Doctor.objects.filter(spec='ทันตแพทย์')
    list7 = Doctor.objects.filter(spec='กุมารแพทย์')
    context = {'list1': list1 ,'list2': list2 ,'list3': list3 ,'list4': list4
               ,'list5': list5 ,'list6': list6 ,'list7': list7 }
    return render(request, "doctors/spec.html", context)

@admin_only
def addDoc(request):
    form = CreateDocForm()
    if request.method == 'POST':
        createDocForm = CreateDocForm(request.POST, request.FILES)
        if createDocForm.is_valid():
            createDocForm.save()
        return redirect("doctors:spec")
    return render(request, "doctors/adddoc.html",{'form': form})


# ยังไม่ได้ใช้
