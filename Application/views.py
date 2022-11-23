from django.shortcuts import render
#  Model
from . models import *
# auth
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request, 'index.html')
def emp_register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password1']

        import random
        max_length = 6
        character = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','y']
        digits = ['0','1','2','3','4','5','6','7','8','9']
        combine_list = character+digits
        generate = [random.choice(combine_list) for i in range(max_length)]
        emp_id = ""
        for item in generate:
            emp_id+=item   
        error = ""
        try:
            new_user = User.objects.create_user(first_name=firstname,last_name=lastname,username=email,password=password) 
            EmployeeDetail.objects.create(user=new_user,emp_id=emp_id) 
            error = "no"
        except:
            error = "yes"     
    return render(request, 'emp_register.html',locals())
    
def emp_login(request):
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['password']
        error = ""
        user = authenticate(username=email,password=password)
        if user:
            login(request,user)
            error = "no"
        else:
            error = "yes"    
    return render(request, 'emp_login.html',locals())