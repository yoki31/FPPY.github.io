from django.urls import path
from . import views

app_name="doctors"
urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('maps', views.maps, name="maps"),
    path('project_requirement', views.project_requirement, name="project_requirement"),
    path('healthblog', views.healthblog, name="healthblog"),
    path('healthblog_one/<pk>', views.healthblog_content, name="healthblog_content"),
    path('healthblog_one', views.healthblog_one, name="healthblog_one"),
    path('news', views.news, name="news"),
    path('news_one/<pk>', views.news_content, name="news_content"),
    path('news_one', views.news_one, name="news_one"),
    path('dpromotion', views.dpromotion, name="dpromotion"),

    # user
    path('userhome', views.userhome, name="userhome"),
    path('umaps', views.umaps, name="umaps"),
    path('uhealthblog', views.uhealthblog, name="uhealthblog"),
    path('uhealthblog_one/<pk>', views.uhealthblog_content, name="uhealthblog_content"),
    path('uhealthblog_one', views.uhealthblog_one, name="uhealthblog_one"),
    path('unews', views.unews, name="unews"),
    path('unews_one/<pk>', views.unews_content, name="unews_content"),
    path('unews_one', views.unews_one, name="unews_one"),
    path('udpromotion', views.udpromotion, name="udpromotion"),

    # admin
    path('adminhome', views.adminhome, name="adminhome"),
    path('mhealthblog', views.mhealthblog, name="mhealthblog"),
    path('edithealthblog', views.edithealthblog, name="edithealthblog"),
    path('edithealthblog/<pk>', views.edithealthblog_content, name="edithealthblog_content"),
    path('deletehealthblog/<pk>', views.deleteArticle, name="deleteArticle"),
    path('addhealthblog', views.addArticle, name="addArticle"),
    path('mnews', views.mnews, name="mnews"),
    path('editnews', views.editnews, name="editnews"),
    path('editnews/<pk>', views.editnews_content, name="editnews_content"),
    path('deleteNews/<pk>', views.deleteNews, name="deleteNews"),
    path('mpromotion', views.mpromotion, name="mpromotion"),
    path('mdoctor', views.mdoctor, name="mdoctor"),
    path('editpromotion', views.editpromotion, name="editpromotion"),
    path('mcustomer', views.mcustomer, name="mcustomer"),

#    path('edithealthblog', views.edithealthblog, name="edithealthblog"), #เดี๋ยวต้องมาแก้pathให้ตามในรายงาน มันแบ่งตามหน้าย่อยนี่จำไม่ได้ว่าเขียนยังไง
#    path('editnews', views.editnews, name="editnews"), #เดี๋ยวต้องมาแก้pathให้ตามในรายงาน มันแบ่งตามหน้าย่อยนี่จำไม่ได้ว่าเขียนยังไง

    # register, login profile
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPLS, name="logout"),
    path('profile', views.profile, name="profile"),
    path('editprofile', views.editprofile, name="editprofile"),

]
