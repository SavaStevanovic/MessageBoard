from django.conf.urls import url

from . import views

app_name = 'board_messages'
urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<board_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^add_board/$', views.add_board, name='add_board'),
    url(r'^(?P<board_id>[0-9]+)/add_list/$', views.add_list, name='add_board'),
    url(r'^list/(?P<list_id>[0-9]+)/$', views.list_card, name='list_card'),
    url(r'^(?P<board_id>[0-9]+)/list/(?P<list_id>[0-9]+)/add_card/', views.add_card, name='add_card'),
    url(r'^(?P<board_id>[0-9]+)/list/(?P<list_id>[0-9]+)/card/(?P<pk>[0-9]+)/edit', views.UpdateCardView.as_view(), name='edit_card'),
    url(r'^(?P<board_id>[0-9]+)/list/(?P<list_id>[0-9]+)/card/(?P<pk>[0-9]+)/delete', views.DeleteCardView.as_view(), name='delete_card'),
]
