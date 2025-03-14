from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# def homepage(request):
#     data={
#         'title': 'Home New',
#         'bdata':'hii i am learning django',
#         'clist':['java','PHP','Python'],
#         'numbers':[],
#         'student':[
#             {'name':'pradeep','phone':968347488},
#             {'name':'niranjan','phone':9683474478},
#         ]
        
#     }

#     return render(request,"index.html",data)


# def aboutUs(request):
#     return render(request,"about.html")
# def course(request):
#     return HttpResponse("course is django")
# def courseDetails(request,courseid):
#     return HttpResponse(courseid)
# def homepage(request):
#     output=0
#     data={}
#     try:
        
#         if request.method == 'POST':
#             n1= int(request.POST.get('num1'))
#             n2=int(request.POST.get('num2'))
#             output=n1+n2
#         data={
#             'n1':n1,
#             'n2':n2,
#             'output':output
            
#             }      
#     except:
#         pass
#     return render(request,'userform.html',data)



# def about_us_view(request):
#     if request.method=="GET":
#         output=request.GET.get('output')
#     return render(request, 'about.html',{'output':output}) 
# # Make sure the template name matches


# def contact_us_view(request):
#     return render(request, 'contact.html') 

# def calculator(request):
#     output = None # Initialize the output variable

#     if request.method == 'POST':
#         try:
#             # Retrieve values from the POST request
#             n1 = eval(request.POST.get('num1',0))  # Using float for calculations
#             n2 = eval(request.POST.get('num2',0))
#             opr = request.POST.get('opr', '')  # Operator from the dropdown

#             # Perform operations based on the operator
#             if opr == "+":
#                 output = n1 + n2
#             elif opr == "-":
#                 output = n1 - n2
#             elif opr == "*":
#                 output = n1 * n2
#             elif opr == "/":
#                 if n2 != 0:  # Check to avoid division by zero
#                     output = n1 / n2
#                 else:
#                     output = "Error: Division by zero"
#         except Exception as e:
#             output = f"Error: {str(e)}"

#     # Render the template with the calculated output
#     return render(request, 'calculator.html', {'output': output})

        


# def userform(request):
#     data={}
#     final=0
#     try:
#         n1=int(request.POST.get("num1"))
#         n2=int(request.POST.get("num2"))
#         final=n1+n2
#         data={
#             "n1":n1,
#             "n2":n2,
#             "output":final
#         }
#         url='/aboutus/?output={}'.format(final)
#         return HttpResponseRedirect(url)
#     except:
#         pass
#     return render(request,"userform.html",data)


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