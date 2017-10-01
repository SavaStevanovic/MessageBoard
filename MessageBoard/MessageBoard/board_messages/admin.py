from django.contrib import admin

# Register your models here.
from .models import Board,List,Card,Category,User,Comment

admin.site.register([Board,List,Card,Category,User,Comment])