from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from .models import *


# Create your views here.

def About(request):
    return render(request,'about.html')


def Contact(request):
    return render(request,'contact.html')


def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    doctors=Doctor.objects.all()
    patient = Patient.objects.all()
    appointment = Appointment.objects.all()

    d = 0;
    p = 0;
    a=0;

    for i in doctors:
         d +=1
    for i in patient:
         p +=1   
    for i in appointment:
         a +=1   
    d1 = {'d':d,'p':p,'a':a}       


    return render(request,'index.html',d1)

def Login(request):
    error=""
    if request.method=='POST':
        u = request.POST['username'] 
        p = request.POST['pass']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"    

        except:
            error="yes"
    d = {'error':error}        
    return render(request,'login.html',d)


def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')

def View_Doctor(request):
        
        if not request.user.is_staff:
            return redirect('login') 
        doc = Doctor.objects.all()
        d = {'doc' :doc}
        return render(request,'view_doctor.html',d) 


def Add_Doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')  
    if request.method=='POST':
        n = request.POST['names']  
        dep = request.POST['department']
        c = request.POST['contact']
        try:    
            Doctor.objects.create(name=n,department=dep,mobile=c)
            error="no"
        except:
            error="yes"
    d = {'error':error}        
    return render(request,'add_doctor.html',d)

def Delete_Doctor(request,pid): 
        if not request.user.is_staff:
            return redirect('login') 
        doctor = Doctor.objects.get(id=pid)
        doctor.delete()
        return render(request,'view_doctor.html') 


def View_Patient(request):
        
        if not request.user.is_staff:
            return redirect('login') 
        pat = Patient.objects.all()
        d = {'pat' :pat}
        return render(request,'view_patient.html',d) 


def Add_Patient(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')  
    if request.method=='POST':
        n = request.POST['name'] 
        g = request.POST['gender'] 
        a = request.POST['age'] 
        r = request.POST['reason'] 
        m = request.POST['mobile'] 
        adm = request.POST['admission'] 
        dis = request.POST['discharge'] 
        docn = request.POST['docname'] 
        pre = request.POST['prescription'] 
        bil = request.POST['bill'] 
        try:    
            Patient.objects.create(name=n,gender=g,age=a,reason=r,mobile=m,admission=adm,discharge=dis,docname=docn,prescription=pre,bill=bil)
            error="no"
        except:
            error="yes"
    d = {'error':error}        
    return render(request,'add_patient.html',d)

def Delete_Patient(request,pid): 
        if not request.user.is_staff:
            return redirect('login') 
        patient = Patient.objects.get(id=pid)
        patient.delete()
        return render(request,'view_patient.html') 




def View_Appointment(request):
        
        if not request.user.is_staff:
            return redirect('login') 
        app = Appointment.objects.all()
        d = {'app' :app}
        return render(request,'view_appointment.html',d) 


def Add_Appointment(request):
    error = ""
    
    # Check if the user is not staff, redirect to login
    if not request.user.is_staff:
        return redirect('login')
    
    # Fetch all doctors and patients to populate the dropdowns
    doctor2 = Doctor.objects.all()
    patient2 = Patient.objects.all()
    
    if request.method == 'POST':
        # Retrieve the form data
        dc = request.POST['doctor'] 
        pa = request.POST['patient'] 
        dt = request.POST['date'] 
        t = request.POST['time'] 

        # Find the corresponding doctor and patient instances
        doctor = Doctor.objects.filter(name=dc).first()
        patient = Patient.objects.filter(name=pa).first()

        if doctor and patient:
            try:
                # Create a new appointment with the correct doctor and patient instances
                Appointment.objects.create(doctor=doctor, patient=patient, date1=dt, time1=t)
                error = "no"
            except Exception as e:
                error = "yes"
                print(f"Error: {e}")  # Optionally log the error for debugging
        else:
            error = "yes"
    
    # Pass the doctors, patients, and any error status back to the template
    d = {'doctor': doctor2, 'patient': patient2, 'error': error}
    return render(request, 'add_appointment.html', d)

def Delete_Appointment(request,pid): 
        if not request.user.is_staff:
            return redirect('login') 
        appointment = Appointment.objects.get(id=pid)
        appointment.delete()
        return render(request,'view_appointment.html') 



