from django.db import models

# Create your models here.
class User(models.Model):
    id=models.AutoField(primary_key=True)
    u_name=models.CharField('Username',max_length=30)
    p_word=models.CharField(_('password'),max_length=30)
    email=models.EmailField('email',max_length=50,unique=True)

    def __str__(self):
        return self.u_name

class Hotel(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField('Username',max_length=30)
    n_tables=models.IntegerField('Number of tables')
    c_no=models.CharField('Contact No',max_length=10)
    r_user=models.ForeignKey('User',on_delete=models.SET_NULL)

    def __str__(self):
        return self.name 

