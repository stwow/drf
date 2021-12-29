from django.urls import path,include
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
app_name = 'dinamo'


urlpatterns = [
    path('all_players/', ShowPlayers.as_view(), name='show_players'),
    path('stadium/', ShowStadium.as_view(), name='show_stadium'),
    path('all_show/', AllShow.as_view(), name='all_show'),
    path('create_player/', PlayerView.as_view(), name = 'player_view'),
    path('create_player/<int:pk>/', PlayerView.as_view(), name = 'player_pk'),
    path('get_player_generic/', GetPlayerGeneric.as_view(), name = 'get_player'),
    path('get_player_viewset/<int:pk>/', player_list_r, name = 'get_viewset_player'),


]

urlpatterns=format_suffix_patterns(urlpatterns)