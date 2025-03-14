from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



def signuppage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!= pass2:
            return HttpResponse("password are unmatched")
        else:
            my_user = User.objects.create_user(username=uname, email=email, password=pass1)
            my_user.save()
            print(uname,email,pass1)
        return redirect('login')
    
    
    
    return render(request,'signup.html')
    
    

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        print(f"Attempting login with: {username}, {pass1}")  # Debugging line

        user = authenticate(request, username=username, password=pass1)
        print(f"User authenticated: {user}")  # Debugging line

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Invalid username or password')

    return render(request, 'login.html')

        
    
        
    
@login_required(login_url='login')
def homepage(request):  # Add request parameter
    return render(request,'home.html')

def logout_view(request):
    logout(request)
    return redirect('login')  
