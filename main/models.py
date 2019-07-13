from django.db import models
# Create your models here.

class User(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField('Username',max_length=30)
    password=models.CharField('password',max_length=30)
    contact=models.CharField('Contact No',max_length=10,blank=True)
    email=models.EmailField('Email',max_length=50,unique=True)
    
    def __str__(self):
        return self.username

class Hotel(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField('Hotel Name',max_length=30)
    password=models.CharField('Password',max_length=30)
    address=models.CharField('Address',max_length=100)
    n_tables=models.IntegerField('Number of tables Available')
    c_no=models.CharField('Contact No',max_length=10,unique=True)
    
    def __str__(self):
        return self.name 

class Reservation(models.Model):
    id=models.AutoField(primary_key=True)
    reservation_hotel=models.IntegerField('Hotel ID',default=0)
    contact = models.TextField('Contact No',max_length=10,blank=True)
    reservation_name=models.CharField('Reservation Name',max_length=30)
    reservation_date=models.CharField('Date and Time',max_length=30)
    reservation_people=models.IntegerField('Number of People',null=True)
