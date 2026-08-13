from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("solutions/", views.solutions, name="solutions"),
    path("projects/", views.projects, name="projects"),
    path("innovation/", views.innovation, name="innovation"),
    path("contact/", views.contact, name="contact"),
]