from django.urls import path
from . import views

app_name="doctors"
urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('maps', views.maps, name="maps"),
    path('project_requirement', views.project_requirement, name="project_requirement"),


#NEW
    path('news', views.news, name="news"),
    path('news/<pk>', views.news_content, name="news_content"),
    path('deleteNews/<pk>', views.deleteNews, name="deleteNews"),
    path('addnews', views.addNews, name="addNews"),
    path('updatenews/<pk>', views.updateNew, name="updateNew"),


#ARTICLE
    path('healthblog', views.healthblog, name="healthblog"),
    path('healthblog/<pk>', views.healthblog_content, name="healthblog_content"),
    path('deletehealthblog/<pk>', views.deleteArticle, name="deleteArticle"),
    path('addhealthblog', views.addArticle, name="addArticle"),
    path('updatehealthblog/<pk>', views.updateArticle, name="updateArticle"),


#PACKAGE
    path('package/', views.package, name="package"),
    path('package/<str:pk>', views.package_content, name="package_content"),
    path('editpackage/<str:pk>', views.editpackage, name="editpackage"),
    path('deletepackage/<str:pk>', views.deletePackage, name="deletepackage"),
    path('addpackage', views.addPackage, name="addPackage"),
    path('buy/<str:pk>', views.buy, name="buy"),
    path('mypack', views.mypack, name="mypack" ),
    path('packbuy', views.packbuy, name="packbuy" ),
    path('packbuy/<str:pk>', views.packbuy_one, name="packbuyone" ),
    path('checkslip/<str:pk>', views.checkslip, name="checkslip" ),
    path('mypack/<str:pk>', views.mypack_one, name="mypackone" ),
    path('sendslip/<str:pk>', views.sendslip, name="sendslip" ),



#Appointment
    path('appointment/<pk>', views.appointment, name="appointment"),
    path('deleteappointment/<pk>', views.deleteAppointment, name="deleteappointment"),
    path('adminappointment', views.adminAppointment, name="mappointment"),
    

    # register, login profile
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPLS, name="logout"),
    path('profile', views.profile, name="profile"),
    path('accsetting', views.account, name="accsetting"),


    path('doctor', views.doctor, name="doctor"),
    path('finddoc', views.finddoc, name="finddoc"),
    path('docprofile/<pk>', views.docprofile, name="docprofile"),
    path('deleteDoc/<pk>', views.deleteDoc, name="deleteDoc"),
    path('spec', views.spec, name="spec"),
    path('addDoc', views.addDoc, name="addDoc"),
    path('updateDoc/<pk>', views.updateDoc, name="updateDoc"),
]

