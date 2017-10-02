from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django import forms
from django.core.exceptions import ObjectDoesNotExist

import datetime

from .models import Category, Board, List_board
from .forms import NameForm

def index(request):
    template_name = 'board_messages/index.html'
    latest_boards_list = Board.objects.order_by('order')
    context = {'latest_boards_list':latest_boards_list,
               'form':NameForm,
               }
    return render(request, template_name, context)

def detail(request, board_id):
    template_name = 'board_messages/detail.html'
    try:
        latest_list_board_list = List_board.objects.filter(board_id=board_id).order_by('order');
    except Exception:
        latest_list_board_list = None;
    context = {'latest_list_board_list':latest_list_board_list,
               'board_id':board_id,
               'form':NameForm,
               }
    return render(request, template_name, context)

    
def add_list(request, board_id):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            list_name = form.cleaned_data.get("Name")
            list_board = Board.objects.get(pk=board_id)
            try:
                latest_list_board_list = List_board.objects.filter(board_id=board_id).count();
            except List_board.DoesNotExist:
                latest_list_board_list = 0;
            List_board.objects.create(board=list_board, name=list_name, order=latest_list_board_list, pub_date=datetime.date.today())
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('board_messages:detail', args=(board_id,)))

    # if a GET (or any other method) we'll create a blank form
    if request.method == 'GET':
        form = NameForm()
        return render(request, 'board_messages:index.html', {'form': form})    
    
def add_board(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            board_name = form.cleaned_data.get("Name")
            board = Board.objects.create(name=board_name, order=Board.objects.count(), pub_date=datetime.date.today())
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('board_messages:detail', args=(board.id,)))

    # if a GET (or any other method) we'll create a blank form
    if request.method == 'GET':
        form = NameForm()
        return render(request, 'board_messages:index.html', {'form': form})
   
