from django.conf.urls import url

from . import views

app_name = 'board_messages'
urlpatterns = [
    # ex: /board_messages/
    url(r'^$', views.index, name='index'),
    # ex: /board_messages/5/
    url(r'^(?P<board_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /board_messages/5/vote/
    url(r'^add_board/$', views.add_board, name='add_board'),
    url(r'^(?P<board_id>[0-9]+)/add_list/$', views.add_list, name='add_board'),
    url(r'^list/(?P<list_id>[0-9]+)/$', views.list_card, name='list_card'),
]