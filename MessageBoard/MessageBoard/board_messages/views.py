from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django import forms

import datetime

from .models import Category, Board
from .forms import BoardForm

def index(request):
    template_name = 'board_messages/index.html'
    latest_boards_list = Board.objects.order_by('-pub_date')[:5]
    context = {'latest_boards_list':latest_boards_list,
               'form':BoardForm,
               }
    return render(request, template_name, context)

class DetailView(generic.DetailView):
    model = Board
    template_name = 'board_messages/detail.html'
    
def add_board(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = BoardForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            board_name = form.cleaned_data.get("board_name")
            board = Board.objects.create(name=board_name, order=Board.objects.count(), pub_date=datetime.date.today())
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('board_messages:detail', args=(board.id,)))

    # if a GET (or any other method) we'll create a blank form
    if request.method == 'GET':
        form = BoardForm()
        return render(request, 'board_messages:index.html', {'form': form})
   
