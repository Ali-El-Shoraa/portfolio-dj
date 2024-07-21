from django.shortcuts import render
# from . import views

# Create your views here.
from .models import Projects, CV


def home(request):
    links = [
        {"key": 1, "name": "Home", "link": "home"},
        {"key": 2, "name": "About", "link": "about"},
        {"key": 3, "name": "Projects", "link": "project"},
        {"key": 4, "name": "Contact", "link": "contact"},
    ]

    links_footer = links[: len(links) - 1]
    social_data = [
        {
            "key": 1,
            "link": "https://www.linkedin.com/in/ali-el-shoraa/",
            "icon": '<i class="fab fa-linkedin"></i>',
        },
        {
            "key": 2,
            "link": "https://github.com/Ali-El-Shoraa",
            "icon": '<i class="fab fa-github"></i>',
        },
        {
            "key": 3,
            "link": "https://wa.me/201550859246",
            "icon": '<i class="fab fa-whatsapp"></i>',
        },
        {
            "key": 4,
            "link": "https://t.me/Ali_El_Shoraa",
            "icon": '<i class="fab fa-telegram-plane"></i>',
        },
        {
            "key": 5,
            "link": "mailto:ali,m.elshoraa@gmail.com",
            "icon": '<i class="fas fa-envelope"></i>',
        },
    ]

    projects = Projects.objects.all()[:3]
    cv = CV.objects.first()
    context = {
        "links": links,
        "social_data": social_data,
        "projects": projects,
        "links_footer": links_footer,
        "cv_url": cv,
    }
    return render(request, "pages/home.html", context)


def projects(request):
    projects = Projects.objects.all()
    return render(request, "pages/projects.html", {"projects": projects})
