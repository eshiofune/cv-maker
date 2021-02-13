from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.files.storage import FileSystemStorage, default_storage
from .models import Education, Work_experience, Projects, Profile
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.

# user_education = Education.objects.all()
# user_work_experience = Work_experience.objects.all()
# user_projects = Projects.objects.all()
# user_profile = Profile.objects.all()


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
    user = request.user

    user_education = Education.objects.filter(userid=user)
    user_work_experience = Work_experience.objects.filter(userid=user)
    user_projects = Projects.objects.filter(userid=user)
    user_profile = Profile.objects.filter(userid=user)

    if user_profile:
        return render(request, 'dashboard.html', {'profile': user_profile[0], 'user_education': user_education, 'user_work_experience': user_work_experience, 'user_projects': user_projects})
    else:
        return render(request, 'dashboard.html', {'profile': user_profile, 'user_education': user_education, 'user_work_experience': user_work_experience, 'user_projects': user_projects})


# a function to logout the user
def logout(request):
    auth.logout(request)
    return redirect('/')

# a function to render the template for CV samples


def createcv(request):
    return render(request, 'createcv.html')


# a function to render and also update the profile table details in the database
def profileform(request):
    user = request.user
    user_profile = Profile.objects.filter(userid=user)
    if user_profile:
        return render(request, 'profileform.html', {'profile': user_profile[0]})
    else:
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
        instance.userid = request.user
        instance.save()
        return redirect('/dashboard/')
    else:
        return render(request, 'eduform.html')


def experience(request):
    if request.method == 'POST':
        start = request.POST['start']
        end = request.POST['end']
        company = request.POST['company']
        role = request.POST['role']
        description = request.POST['description']

        exe = Work_experience(start=start, end=end, company=company, role=role,
                              description=description)
        instance = exe
        instance.userid = request.user
        instance.save()
        return redirect('/dashboard/')
    else:
        return render(request, 'expform.html')


def projects(request):
    if request.method == 'POST':
        project_name = request.POST['project_name']
        description = request.POST['description']

        pro = Projects(project_name=project_name, description=description)

        instance = pro
        instance.userid = request.user
        instance.save()
        return redirect('/dashboard/')
    else:
        return render(request, 'projform.html')


def profile(request, id):
    if request.method == 'POST':
        if id == 0:

            title = request.POST['title']
            address = request.POST['address']
            mobile = request.POST['mobile']
            image = request.FILES['image']
            nationality = request.POST['nationality']
            state = request.POST['state']
            skills = request.POST['skills']
            hobbies = request.POST['hobbies']
            references = request.POST['references']

            fs = FileSystemStorage()
            name = fs.save(image.name, image)
            image_url = fs.url(name)
            pro = Profile(title=title, address=address, mobile=mobile, image=image_url, nationality=nationality,
                          state=state, skills=skills, hobbies=hobbies, references=references, img_name=name)

            instance = pro
            instance.userid = request.user
            instance.save()
            return redirect('/dashboard/')

        else:
            title = request.POST['title']
            address = request.POST['address']
            mobile = request.POST['mobile']
            image = request.FILES['image']
            nationality = request.POST['nationality']
            state = request.POST['state']
            skills = request.POST['skills']
            hobbies = request.POST['hobbies']
            references = request.POST['references']

            # getting the user profile so as to delete the previous image they uploaded before uploading a new one
            user = request.user
            user_profile = Profile.objects.filter(userid=user)
            person = user_profile[0]
            default_storage.delete(str(person.img_name))

            fs = FileSystemStorage()
            name = fs.save(image.name, image)
            image_url = fs.url(name)
            pro = Profile.objects.filter(userid=id)
            pro.update(title=title, address=address, mobile=mobile, image=image_url, nationality=nationality,
                       state=state, skills=skills, hobbies=hobbies, references=references, img_name=name)
            print('inserted')
            return redirect('/dashboard/')
    else:
        return redirect('/dashboard/')


# a function to render the individual templates depending on which one the user selected
def temp(request, id):
    user = request.user

    user_education = Education.objects.filter(userid=user)
    user_work_experience = Work_experience.objects.filter(userid=user)
    user_projects = Projects.objects.filter(userid=user)
    user_profile = Profile.objects.filter(userid=user)

    if id == 1:
        if user_profile:
            return render(request, 'temps/temp1.html', {'profile': user_profile[0], 'user_education': user_education, 'user_work_experience': user_work_experience, 'user_projects': user_projects})
        else:
            return render(request, 'temps/temp1.html', {'profile': user_profile, 'user_education': user_education, 'user_work_experience': user_work_experience, 'user_projects': user_projects})
    elif id == 2:
        if user_profile:
            return render(request, 'temps/temp2.html', {'profile': user_profile[0], 'user_education': user_education, 'user_work_experience': user_work_experience, 'user_projects': user_projects})
        else:
            return render(request, 'temps/temp2.html', {'profile': user_profile, 'user_education': user_education, 'user_work_experience': user_work_experience, 'user_projects': user_projects})

    elif id == 3:
        if user_profile:
            return render(request, 'temps/temp3.html', {'profile': user_profile[0], 'user_education': user_education, 'user_work_experience': user_work_experience, 'user_projects': user_projects})
        else:
            return render(request, 'temps/temp3.html', {'profile': user_profile, 'user_education': user_education, 'user_work_experience': user_work_experience, 'user_projects': user_projects})


def edudelete(request, id):
    education = Education.objects.get(pk=id)
    education.delete()
    return redirect('/dashboard/')


def expdelete(request, id):
    experience = Work_experience.objects.get(pk=id)
    experience.delete()
    return redirect('/dashboard/')


def projdelete(request, id):
    project = Projects.objects.get(pk=id)
    project.delete()
    return redirect('/dashboard/')
