from django.db import models
from django.utils import timezone

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=40)
    department = models.CharField(max_length=40)
    mobile = models.IntegerField()

    def __str__(self):
        return self.name
    

    
class Patient(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=12)
    age = models.IntegerField()
    reason = models.CharField(max_length=700, default="Unknown")
    mobile = models.IntegerField(null=True)
    admission = models.DateField(default=timezone.now)
    discharge = models.DateField(default=timezone.now)
    docname = models.CharField(max_length=100, default="Unknown Doctor")
    prescription = models.CharField(max_length=700, default="No prescription")
    bill = models.FloatField(default=0.0)


    def __str__(self):
        return self.name
    

class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    date1 = models.DateField()
    time1= models.TimeField()
   

    def __str__(self):
        return self.doctor.name+"--"+self.patient.name