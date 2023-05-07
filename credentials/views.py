from django.shortcuts import render ,  redirect
from django.contrib.auth.models import User,auth 
from django.contrib import messages

# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')
def login(request):
    if request.method == 'POST':
        usernam =request.POST['username']
        pasword =request.POST['password']
        callauthuser =auth.authenticate(username=usernam,password=pasword)

        if callauthuser  is not None:
            auth.login(request,callauthuser)
            return redirect('/')
        else:
            messages.info(request,"inavalid credentials")
            return redirect('login')

    return render(request,"login.html")

def  register(request):
    if request.method == 'POST':
        Username = request.POST['UserName']
        Firstname = request.POST['firstName']
        Lastname = request.POST['lastName']
        Email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=Username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
        
            elif User.objects.filter(email=Email).exists():
                messages.info(request,"Email Taken")
                return redirect('register') 
            else:  
                user=User.objects.create_user( username = Username ,first_name = Firstname,password = password,last_name = Lastname,email =Email)
                user.save()
                return redirect('login')
            
        else:
            messages.info(request , "password not matching")
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')