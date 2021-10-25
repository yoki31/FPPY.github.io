from django.urls import path
from . import views

app_name="doctors"
urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('maps', views.maps, name="maps"),
    path('project_requirement', views.project_requirement, name="project_requirement"),
]
