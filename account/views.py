
from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login as dj_login,logout as dj_logout
# from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    
    return render(request, 'index1.html')

def signup(request):
    if request.method =='POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse(" Passwords doesn't matched!!!! ")
        else:
            my_user = User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'sign up.html')



def login(request):
     if request.method =='POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request,username=username,password=pass1)

        if user is not None:
            dj_login(request, user)
            return redirect('home')
        else:
            return HttpResponse(" Username or Password is incorrect!!! ")

     return render(request, 'login.html')


# def adminlogin(request):
#      if request.method =='POST':
#         username = request.POST.get('username')
#         pass1= request.POST.get('password')
#         user = authenticate(request,username=username,password=pass1)

#         if user is not None:
#             dj_login(request, user)
#             return redirect(' #   ')
#         else:
#             return HttpResponse(" Username or Password is incorrect!!! ")

#      return render(request, 'adminlogin.html')



def logout(request):
    dj_logout(request)
    return redirect('login')  
   