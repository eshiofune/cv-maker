from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Education, Work_experience, Projects, Profile
# Create your views here.

user_education = Education.objects.all()
user_work_experience = Work_experience.objects.all()
user_projects = Projects.objects.all()
user_profile = Profile.objects.all()


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
                return redirect('/dashboard/')
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
            return redirect('/dashboard/')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('/login/')
    else:
        return render(request, 'login.html')


# a function to render the dashboard template
def dashboard(request):
    return render(request, 'dashboard.html', {'user_profile': user_profile, 'user_education': user_education, 'user_work_experience': user_work_experience, 'user_projects': user_projects})


# a function to logout the user
def logout(request):
    auth.logout(request)
    return redirect('/')


# a function to render the template for CV samples
def createcv(request):
    return render(request, 'createcv.html')


# a function to render and also update the profile table details in the database
def profileform(request):
    return render(request, 'profileform.html')


def education(request):
    if request.method == 'POST':
        start = request.POST['start']
        end = request.POST['end']
        school = request.POST['school']
        descipline = request.POST['descipline']

        edu = Education(start=start, end=end, school=school,
                        descipline=descipline)

        instance = edu
        instance.user_id = request.user
        instance.save()
        return redirect('/dashboard/')
    else:
        return redirect('/dashboard/')


def experience(request):
    if request.method == 'POST':
        start = request.POST['start']
        end = request.POST['end']
        company = request.POST['school']
        role = request.POST['descipline']
        description = request.POST['descipline']

        exe = Work_experience(start=start, end=end, company=company, role=role,
                              description=description)
        instance = exe
        instance.user_id = request.user
        instance.save()
        return redirect('/dashboard/')
    else:
        return redirect('/dashboard/')


def projects(request):
    if request.method == 'POST':
        project_name = request.POST['project_name']
        description = request.POST['description']

        pro = Projects(project_name=project_name, description=description)

        instance = pro
        instance.user_id = request.user
        instance.save()
        return redirect('/dashboard/')
    else:
        return redirect('/dashboard/')


def profile(request):
    if request.method == 'POST':

        title = request.POST['title']
        address = request.POST['address']
        mobile = request.POST['mobile']
        image = request.POST['image']
        nationality = request.POST['nationality']
        state = request.POST['state']
        skills = request.POST['skills']
        hobbies = request.POST['hobbies']
        references = request.POST['references']

        pro = Profile(title=title, address=address, mobile=mobile, image=image, nationality=nationality,
                      state=state, skills=skills, hobbies=hobbies, references=references)

        instance = pro
        instance.user_id = request.user
        instance.save()
        return redirect('/dashboard/')
    else:
        return redirect('/dashboard/')
