from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from re import compile

import datetime

from .models import Category, Board, List_board, Card
from .forms import NameForm, UpdateForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/messages/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def index(request):
    template_name = 'board_messages/index.html'
    latest_boards_list = Board.objects.order_by('order')
    context = {'latest_boards_list':latest_boards_list,
               'form':NameForm,
               }
    return render(request, template_name, context)

class DeleteCardView(generic.DeleteView):
    model = Card
    form=UpdateForm
    template_name = 'board_messages/card.html'
    
    def get_success_url(self):
        return reverse('board_messages:detail', kwargs={'board_id':self.kwargs['board_id']})

class UpdateCardView(generic.UpdateView):
    model = Card
    fields=['card_text']
    form=UpdateForm
    template_name = 'board_messages/card.html'
    
    def get_success_url(self):
        return reverse('board_messages:detail', kwargs={'board_id':self.kwargs['board_id']})
    
    def get_context_data(self, **kwargs):
        context = super(UpdateCardView, self).get_context_data(**kwargs)
        context['list'] = List_board.objects.get(id=context['card'].list_id)
        context['list_id']=self.kwargs['list_id']
        context['board_id']=self.kwargs['board_id']
        return context 
    
@login_required 
def list_card(request, board_id, list_id):
    template_name = 'board_messages/list_card.html'
    try:
        latest_card_list = Card.objects.filter(list_id=list_id).order_by('order');
    except Exception:
        latest_card_list = None;
    context = {'latest_card_list':latest_card_list,
               'list_id':list_id,
               'card_form':NameForm,
               'board_id':board_id,
               }
    return render(request, template_name, context)

@login_required 
def add_card(request, board_id, list_id):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            card_name = form.cleaned_data.get("Name")
            list_board = List_board.objects.get(pk=list_id)
            latest_card_list = Card.objects.filter(list_id=list_id).count();
            Card.objects.create(list=list_board, name=card_name, order=latest_card_list, pub_date=datetime.date.today())
            # redirect to a new URL:
            return HttpResponseRedirect(reverse('board_messages:detail', args=(board_id,)))

    # if a GET (or any other method) we'll create a blank form
    if request.method == 'GET':
        form = NameForm()
        return render(request, 'board_messages:index.html', {'form': form})    

def detail(request, board_id):
    template_name = 'board_messages/detail.html'
    try:
        latest_list_board_list = List_board.objects.filter(board_id=board_id).order_by('order');
    except Exception:
        latest_list_board_list = None;
    list_list_board_id = latest_list_board_list.values('id');
    card_list = Card.objects.filter(list_id__in=list_list_board_id);
    context = {'latest_list_board_list':latest_list_board_list,
               'board_id':board_id,
               'form':NameForm,
               'card_list':card_list
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
   
