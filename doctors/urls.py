from django.urls import path
from . import views

app_name="doctors"
urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('maps', views.maps, name="maps"),
    path('project_requirement', views.project_requirement, name="project_requirement"),
    path('healthblog', views.healthblog, name="healthblog"),
    path('news', views.news, name="news"),

    # user
    path('userhome', views.userhome, name="userhome"),
    path('uhealthblog', views.uhealthblog, name="uhealthblog"),
    path('unews', views.unews, name="unews"),

    # admin
    path('mhealthblog', views.mhealthblog, name="mhealthblog"),
    path('mnews', views.mnews, name="mnews"),
    
    path('edithealthblog', views.edithealthblog, name="edithealthblog"), #เดี๋ยวต้องมาแก้pathให้ตามในรายงาน มันแบ่งตามหน้าย่อยนี่จำไม่ได้ว่าเขียนยังไง
    path('editnews', views.editnews, name="editnews"), #เดี๋ยวต้องมาแก้pathให้ตามในรายงาน มันแบ่งตามหน้าย่อยนี่จำไม่ได้ว่าเขียนยังไง
    
]
