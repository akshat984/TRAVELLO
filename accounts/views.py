from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
def register(request):
    if request.method == 'POST':
        fn = request.POST['first_name']
        ln = request.POST['last_name']
        un = request.POST['user_name']
        p1 = request.POST['password1']
        p2 = request.POST['password2']
        email = request.POST['email']


        if p1==p2:
            if User.objects.filter(username=un).exists():
                messages.info(request,'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=un,password=p1,email=email,first_name=fn,last_name=ln)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password not matching')
            return redirect('register')

    else:
        return render(request,"register.html")
def login(request):
    if request.method=='POST':
        un = request.POST['username']
        p1 = request.POST['password']
        user = auth.authenticate(username=un,password=p1)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid')
            return redirect('login')
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
# Create your views here.
