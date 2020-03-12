from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password_repeat = request.POST['password_repeat']

        if password != password_repeat:

            print('password not matching')
            messages.info(request, 'password not matching')
            return redirect('/signup/')

        elif User.objects.filter(email=email).exists():

            print('Email already exists')
            messages.info(request, 'Email already exists')
            return redirect('/signup/')

        elif User.objects.filter(username=username).exists():

            print('Username already exists')
            messages.info(request, 'Username already exists')
            return redirect('/signup/')

        else:
            user = User.objects.create_user(
                first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.save()
            print('user created')
            return redirect('/login/')

    else:
        return render(request, 'signup.html')


# def login(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']

#         user = auth.authenticate(email=email, password=password)

#         if user is not None:
#             auth.login(request, user)
#             return redirect(request, '/')
#         else:
#             messages.info(request, 'Invalid Email or Password')
#             return redirect('/login/')

#     else:
#         return render(request, 'login.html')
