from django.shortcuts import render,redirect
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
            EmployeeEducation.objects.create(user=new_user)
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

def emp_Interface(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    return render(request, 'emp_Interface.html',locals())   

def emp_changePassword(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    error = ""
    user = request.user   
    if request.method == "POST":
        current = request.POST['currentPassowrd']
        newPass = request.POST['newPassword']
        try:
            if user.check_password(current):
                user.set_password(newPass)
                user.save()
                error = "no"
            else:
                error = "not"    
        except:
            error = "yes"   
    return render(request, 'emp_changePassword.html',locals())      

def emp_logout(request):
    logout(request)
    return redirect('index')

def emp_profile(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    user = request.user #current user
    employee = EmployeeDetail.objects.get(user=user)
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        contact = request.POST['contact']
        gender = request.POST['gender']
        designation = request.POST['designation']
        department = request.POST['department']
        joiningDate = request.POST['joiningDate']

        # Update changes:
        employee.user.first_name = firstname
        employee.user.last_name = lastname
        employee.user.username = email
        employee.contact = contact
        employee.designation = designation
        employee.department = department

        if joiningDate:
             employee.joiningDate = joiningDate
        if gender!="none":
             employee.gender = gender          
             
        try:
            employee.save()
            employee.user.save()
            error = "no"
        except:
            error = "yes"    

    return render(request, 'emp_profile.html',locals()) 

def emp_education(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    user = request.user #current user
    education = EmployeeEducation.objects.get(user=user)
    return render(request, 'emp_education.html',locals())    
    
def edit_Education(request):
    if not request.user.is_authenticated:
        return redirect('emp_login')
    color = "primary"
    error = ""    
    user = request.user #current user
    education = EmployeeEducation.objects.get(user=user)
    if request.method == "POST":
        # PG
        coursenamePG = request.POST['coursenamePG']
        collegePG = request.POST['collegePG']
        marksPG = request.POST['marksPG']
        passoutPG = request.POST['passoutPG']
        # G
        coursenameG = request.POST['coursenameG']
        collegeG = request.POST['collegeG']
        marksG = request.POST['marksG']
        passoutG = request.POST['passoutG']
        # HSC
        coursenameHSC = request.POST['coursenameHSC']
        collegeHSC = request.POST['collegeHSC']
        marksHSC = request.POST['marksHSC']
        passoutHSC = request.POST['passoutHSC']
        # SSC
        coursenameSSC = request.POST['coursenameSSC']
        collegeSSC = request.POST['collegeSSC']
        marksSSC = request.POST['marksSSC']
        passoutSSC = request.POST['passoutSSC']
        # Update Data
       
        # Update changes:
        education.CoursenamePG = coursenamePG
        education.CollegePG = collegePG
        education.ScorePG = marksPG
        education.PassoutPG = passoutPG

        education.CoursenameG = coursenameG
        education.CollegeG = collegeG
        education.ScoreG = marksG
        education.PassoutG = passoutG

        education.CoursenameHSC = coursenameHSC
        education.CollegeHSC = collegeHSC
        education.ScoreHSC = marksHSC
        education.PassoutHSC = passoutHSC

        education.CoursenameSSC = coursenameSSC
        education.CollegeSSC = collegeSSC
        education.ScoreSSC = marksSSC
        education.PassoutSSC = passoutSSC
    
        try:
            education.save()
            error = "no"
            color = "success"
        except:
            error = "yes"  
            color = "danger"  
            print("exception : ",e)
    return render(request, 'edit_Education.html',locals())    
