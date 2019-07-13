from django import forms
from main.models import User,Hotel,Reservation

class UserCreate(forms.ModelForm):
    password = forms.CharField(label='Password',
    widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    class Meta:
        model = User
        fields = ('username','email','contact','password')
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control','autofocus':'true','placeholder':'Username'}),
            'contact': forms.TextInput(attrs={'class':'form-control','maxlength':'10','placeholder':'Contact No'}),
            'email': forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}),
        }

class Hotelcreate(forms.ModelForm):
    password = forms.CharField(label='Password',
    widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    class Meta:
        model = Hotel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','autofocus':'True','placeholder':'Hotel Name'}),
            'address': forms.Textarea(attrs={'class':'form-control','placeholder':'Address Of Hotel','rows':'5','cols':'40'}),
            'n_tables': forms.NumberInput(attrs={'class':'form-control','placeholder':'Number Of Tables Available'}),
            'c_no': forms.TextInput(attrs={'class':'form-control','placeholder':'Contact No'}),
        }

class Hotellogin(forms.ModelForm):
    password = forms.CharField(label='Password',
    widget = forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    class Meta:
        model = Hotel
        fields = ('name','password',)
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','autofocus':'True','placeholder':'Hotel Name'})
        }


class UserLoginForm(forms.ModelForm):
    class Meta:
        model= User
        fields=('username','password')
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control','maxlength':'50','placeholder':'Username'}),
            'password':forms.PasswordInput(attrs={'class':'form-control','maxlength':'30','placeholder':'Password'}),
        }


class TablesUpdate(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ('n_tables',)
        widgets = {
            'n_tables': forms.NumberInput(attrs={'class':'form-control','placeholder':'Number Of Tables Available'})
        }

class reservation(forms.Form):
    reservation_name=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','maxlength':'30','placeholder':'Name'}))
    contact = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','maxlength':'10','placeholder':'Contact No'}))
    reservation_date=forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control','maxlength':'30','placeholder':'Date and Time'}))
    reservation_people=forms.IntegerField(label='',widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Number of People'}))