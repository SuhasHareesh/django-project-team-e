from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login,logout
from main.forms import UserCreate,Hotelcreate,Hotellogin,TablesUpdate,reservation,UserLoginForm
from main.models import User,Hotel,Reservation
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

#Home view
def home(request):
        if request.session.has_key('usename'):
                username=request.session['usename']
                return render(request,'home2.html',{'username':username,'hoteluser':Hotel.objects.all})
        elif request.session.has_key('hotelname'):
                hotelname=request.session['hotelname']
                user = Hotel.objects.get(name=hotelname)
                if Reservation.objects.filter(reservation_hotel=user.id):
                    rtable=True
                return render(request,'home1.html',{'hotel':user.n_tables,'name':hotelname,'id':user.id,'table':rtable,'update1':True,'reservations':Reservation.objects.filter(reservation_hotel=user.id)})
        else:
                messages.success(request,'Welcome Back!')
                return render(request,'home.html')

# User Registration
def createuser(request):
    if request.method == 'POST':
        form = UserCreate(request.POST)
        if form.is_valid():
            user = User.objects.create(username = form.cleaned_data.get('username'),
            password = form.cleaned_data.get('password'),
            contact=form.cleaned_data.get('contact'),
            email = form.cleaned_data.get('email'))
            user.save()
            messages.success(request,'Created Successfully!')
            return redirect('/')
        else:
            print(form.errors)
    else:
        form = UserCreate()
    return render(request,'signup.html',{'form':form,'value':'Register','signup':True})


# Hotel Registration
def createhotel(request):
    if request.method == 'POST':
        form = Hotelcreate(request.POST)
        if form.is_valid():
            user = Hotel.objects.create(name = form.cleaned_data.get('name'),
            password = form.cleaned_data.get('password'),
            address = form.cleaned_data.get('address'),
            n_tables= form.cleaned_data.get('n_tables'),
            c_no = form.cleaned_data.get('c_no'))
            user.save()
            messages.success(request,'Created Successfully !')
            return render(request,'home.html')
        else:
            print(form.errors)
    else:
        form = Hotelcreate()
        return render(request,'signup.html',{'form':form,'value':'Create','signup':True})


# Hotel Login
def hotellogin(request):
    rtable=False
    hotelname='not logged in'
    if request.method == 'POST':
        form = Hotellogin(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            request.session['hotelname'] = name
            password = form.cleaned_data.get('password')
            user = Hotel.objects.get(name=name)
            if Reservation.objects.filter(reservation_hotel=user.id):
                rtable=True
            if user.password == password:
                messages.success(request,'Logged In Successfully !')
                return render(request,'home1.html',{'hotel':user.n_tables,'name':name,'id':user.id,'table':rtable,'update1':True,'reservations':Reservation.objects.filter(reservation_hotel=user.id)})
            else:
                messages.warning(request,'Invalid Hotel Name or Password. ')
                return redirect('/hotellogin/')
        else:
            print(form.errors)
            messages.warning(request,'Error. Sorry for Inconvenience.')
            return redirect('/')
    else:
        form = Hotellogin()
        return render(request,'signup.html',{'form':form,'value':'Login','login':True})


# User Login
def userlogin(request):
    usename='not logged in'
    if request.method=='POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get('username')
            usename = uname
            request.session['usename'] = usename
            pword=form.cleaned_data.get('password')
            user=User.objects.get(username=uname)
            if(user.password==pword):
                messages.success(request,'Logged in Successfully !')
                return render(request,'home2.html',{'hoteluser':Hotel.objects.all(),'username':usename})
            else:
                messages.warning(request,'Invalid Username or Password.')
                return redirect('/userlogin/')
        else:
            print(form.errors)
            messages.warning(request,'Error. Sorry for Inconvenience. ')
            return redirect('/')
    else:
            form=UserLoginForm()
            return render(request,'signup.html',{'form':form,'value':'Login','login':True})

def table(request,id):
    rtable=False
    user = Hotel.objects.get(id=id)
    if request.method == 'POST':
        form = TablesUpdate(request.POST)
        if form.is_valid():
            n_tables =form.cleaned_data.get('n_tables')
            user.n_tables = n_tables
            user.save()
            if Reservation.objects.filter(reservation_hotel=id):
                rtable=True
            messages.success(request,'Number of tables Updated.')
            return render(request,'home1.html',{'hotel':user.n_tables,'name':user.name,'table':rtable,'update1':True,'reservations':Reservation.objects.filter(reservation_hotel=id)})
        else:
            print(form.errors)
    else:
        form = TablesUpdate()
        return render(request,'home1.html',{'hotel':user.n_tables,'name':user.name,'form':form,'value':'Update','update':True,'table':rtable})

def view(request,id):
    if request.session.has_key('usename'):
        uname = request.session['usename']
    user = Hotel.objects.get(id=id)
    return render(request,'reservation.html',{'username':uname,'details':True,'user':user})
# Reservation 
def reserveseat(request,id):
    if request.session.has_key('usename'):
        uname = request.session['usename']
    user=User.objects.get(username=uname)
    if request.method=='POST':
        form=reservation(request.POST)
        if form.is_valid():
            
            userr=Reservation.objects.create(reservation_name=form.cleaned_data.get('reservation_name'),
            contact = form.cleaned_data.get('contact'),
            reservation_people=form.cleaned_data.get('reservation_people'),
            reservation_date=form.cleaned_data.get('reservation_date'),reservation_hotel=id
            )
            userr.save()
            hotel=Hotel.objects.get(id=id)
            string='You Tables have been Reserved at '+hotel.name+' on '+userr.reservation_date+' in the name of '+userr.reservation_name+' and the hotel address is '+hotel.address
            email(request,string,user.email)
            # messages.success(request,string)
            return render(request,'home2.html',{'hoteluser':Hotel.objects.all(),'username':uname})
    else:
        form=reservation()
        return render(request,'reservation.html',{'form':form,'username':uname,'details':False})

def delete(request,name,id):
    user = Hotel.objects.get(id=id)
    userr = Reservation.objects.get(id=name).delete()
    if userr:
        rtable=True
    return render(request,'home1.html',{'hotel':user.n_tables,'name':user.name,'id':user.id,'table':rtable,'update1':True,'reservations':Reservation.objects.filter(reservation_hotel=user.id)})

def logoutt(request):
    if request.session.has_key('usename'):
        del request.session['usename']
    elif request.session.has_key('hotelname'):
        del request.session['hotelname']
    messages.success(request,'You Have Been Logged Out.')
    return redirect('/')

def email(request,string,emailid):
    subject = 'Thank you for Reserving !'
    message = string
    email_from = 'Hotel Reserver'
    recipient_list = [emailid,]  
    send_mail( subject, message, email_from, recipient_list )
    return 
