from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

#  A function to render the home.html template


def home(request):
    return render(request, 'home.html')


# A function to render the signup page
# its also gonna receive the post request from the signup form
def signup(request):

    # statement to check if the request is for form POST or a GET
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        password_repeat = request.POST['password_repeat']

        # conditions to check if the credentials supplied to the form are valid
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
            # if there is no problem with any of the supplied details, the django built-in ORM creates the user account and stores the details in the database
            user = User.objects.create_user(
                first_name=first_name, last_name=last_name, email=email, username=username, password=password)
            user.save()
            print('user created')
            if user.is_active:
                auth.login(request, user)
                return redirect('/')

    else:
        return render(request, 'signup.html')


# a function to render the login page
# it'll also accept a POST request from the login page to authenticate a user
def login(request):
    # condition to check if the request is a POST or a GET
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print('got here')
            return redirect('/')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('/login/')
    else:
        return render(request, 'login.html')


# a function to logout the user
def logout(request):
    auth.logout(request)
    return redirect('/')
