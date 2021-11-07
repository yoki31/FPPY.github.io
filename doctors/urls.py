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



    path('mdoctor', views.mdoctor, name="mdoctor"),
    
    path('mcustomer', views.mcustomer, name="mcustomer"),

#    path('edithealthblog', views.edithealthblog, name="edithealthblog"), #เดี๋ยวต้องมาแก้pathให้ตามในรายงาน มันแบ่งตามหน้าย่อยนี่จำไม่ได้ว่าเขียนยังไง
#    path('editnews', views.editnews, name="editnews"), #เดี๋ยวต้องมาแก้pathให้ตามในรายงาน มันแบ่งตามหน้าย่อยนี่จำไม่ได้ว่าเขียนยังไง

    # register, login profile
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPLS, name="logout"),
    path('profile', views.profile, name="profile"),
    path('accsetting', views.account, name="accsetting"),

]

