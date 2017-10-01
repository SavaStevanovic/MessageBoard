from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Category, Board

def index(request):
    latest_boards_list = Board.objects.order_by('order')[:5]
    context = {
        'latest_boards_list': latest_boards_list,
    }
    return render(request, 'board_messages/index.html', context)

def detail(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    return render(request, 'board_messages/detail.html', {'board': board})

def results(request, board_id):
    response = "You're looking at the results of board %s."
    return HttpResponse(response % board_id)

def vote(request, board_id):
    return HttpResponse("You're voting on board %s." % board_id)
