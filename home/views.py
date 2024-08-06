from django.shortcuts import render,redirect,get_object_or_404
from . models import Todo
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import re 


# Create your views here.
@login_required(login_url='signin/')
def index(request):
    todo=Todo.objects.filter(user=request.user).all()
    if request.POST:
        title=request.POST.get('title')
        user=request.user
        Todo.objects.create(title=title, user=user)
        return render(request,'index.html',{'todo':todo})
    return render(request,'index.html',{'todo':todo})

@login_required(login_url='signin/')
def edit(request,pk):
    instance=Todo.objects.get(pk=pk)
    if request.POST:
        title=request.POST['title']
        instance.title=title
        instance.save()    
        return redirect('home')
    else:
        value=instance.title
        return render(request,'index.html',{'value':value})

@login_required(login_url='signin/')
def delete(request,pk):
    instance=Todo.objects.get(pk=pk)
    instance.delete()
    return redirect('home')

def validate_username(username):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex,username):
        return "Invalid email address"
    if User.objects.filter(username=username).exists():
        return "A user with that username already exists."
    return None

def validate_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    if not re.search(r'\d', password):
        return "Password must contain at least one digit."
    if not re.search(r'[A-Z]', password):
        return "Password must contain at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return "Password must contain at least one lowercase letter."
    if not re.search(r'[!@#$%^&*()_+=-]', password):
        return "Password must contain at least one special character (!@#$%^&*()_+=-)."
    return None

def signin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        try:
            user=authenticate(request,username=username,password=password)
            if user is not None: 
                login(request,user)
                return redirect('home')
            else:
                if not User.objects.filter(username=username).exists():
                    messages.error(request,"Invalid username")
                else:
                    messages.error(request,"Invalid password")
                return render(request,'signin.html',{'username':username})
        except:
            messages.error(request,"Something went wrong. Try again")
    return render(request,'signin.html')

def signup(request):
    validation=True
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('password2')
        username_error = validate_username(username)
        password_error = validate_password(password)

        if username_error:
            validation=False
            messages.error(request, username_error)
        elif password_error:
            validation=False
            messages.error(request, password_error)
        elif confirm_password != password:
             validation=False
             messages.error(request, "Passwords do not match.")
        else:
            
            my_user=User.objects.create_user(username=username,password=password)
            my_user.first_name=fname
            my_user.last_name=lname
            my_user.email=username
            my_user.save()
            # subject = 'Registration Successful'
            # message = 'You have successfully signed up in Todo Application. You can Login to experience the Application'
            # recipient = my_user.email
            # send_mail(subject, 
            # message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'Registration Successful!')
            return redirect('signin')
            # except:
            #     messages.error(request,"Something went wrong. Try again")
            #     return redirect('signup')
        if not validation:
            context={
                'fname':fname,
                'lname':lname,
                'username':username
            }
            return render(request,'signup.html',context)
    return render(request,'signup.html')

@login_required(login_url='signin/')
def signout(request):
    logout(request)
    return redirect('signin')

