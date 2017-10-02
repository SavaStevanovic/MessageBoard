from django.conf.urls import url

from . import views

app_name = 'board_messages'
urlpatterns = [
    # ex: /board_messages/
    url(r'^$', views.index, name='index'),
    # ex: /board_messages/5/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    # ex: /board_messages/5/vote/
    url(r'^add_board/$', views.add_board, name='add_board'),
]