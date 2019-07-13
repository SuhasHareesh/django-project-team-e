from django.contrib import admin

# Register your models here.
from main.models import User,Hotel,Reservation
admin.site.register(User)
admin.site.register(Hotel)
admin.site.register(Reservation)