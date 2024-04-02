from django.urls import path
from . import views
app_name = 'game'

urlpatterns = [
    path('user/', views.UserView.as_view(), name='user-view'),
    path('team/', views.TeamView.as_view(), name='team-view'),
]