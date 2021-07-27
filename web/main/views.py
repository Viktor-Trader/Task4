from django.shortcuts import render
from .models import Users

def front(request):
    users = Users.objects.all()
    return render(request, 'main/front.html', {'title': 'The main page PeopleIN', 'users': users})


def about(request):
    return render(request, 'main/about.html')


def registration(request):
    return render(request, 'main/registration.html')
