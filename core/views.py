from django.shortcuts import render
from .models import HomepageSlide


def home(request):
    slides = HomepageSlide.objects.filter(
        is_active=True
    ).order_by("display_order", "title")

    return render(
        request,
        "core/home.html",
        {
            "slides": slides,
        }
    )


def about(request):
    return render(request, "core/about.html")


def services(request):
    return render(request, "core/services.html")


def solutions(request):
    return render(request, "core/solutions.html")


def projects(request):
    return render(request, "core/projects.html")


def innovation(request):
    return render(request, "core/innovation.html")


def contact(request):
    return render(request, "core/contact.html")
