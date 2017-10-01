from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /board_messages/
    url(r'^$', views.index, name='index'),
    # ex: /board_messages/5/
    url(r'^(?P<board_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /board_messages/5/results/
    url(r'^(?P<board_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /board_messages/5/vote/
    url(r'^(?P<board_id>[0-9]+)/vote/$', views.vote, name='vote'),
]