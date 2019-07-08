from django import forms

class UserCreate(forms.Form):
    uname=forms.CharField(label='',
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username','max_length':'30'}))
    email=forms.EmailField(label='',
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email','max_length':'30'}))
    pword=forms.CharField(label='',
    widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','max_length':'30'}))