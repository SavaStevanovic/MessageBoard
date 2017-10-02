from django.contrib import admin

# Register your models here.
from .models import Board,List_board,Card,Category,User,Comment

admin.site.register([Board,List_board,Card,Category,User,Comment])