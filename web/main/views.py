from django.shortcuts import render, redirect
from .models import Users
from .forms import UsersForm

def front(request):
    users = Users.objects.all()
    return render(request, 'main/front.html', {'title': 'The main page PeopleIN', 'users': users})


def about(request):
    return render(request, 'main/about.html')


def registration(request):
    error = ''
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'error in filling out the registration form'

    form = UsersForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/registration.html', context)
