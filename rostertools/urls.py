from django.urls import path
from . import views

app_name='rostertools'
urlpatterns = [
    path('', views.RosterListView.as_view(), name='index'),
    path('roster/<int:pk>/', views.RosterDetailView.as_view(), name='view roster'),
    path('users/', views.UsersListView.as_view(), name='users'),
    path('users/<str:username>/', views.UserRosterListView.as_view(), name='user'),
    path('rosters/add/', views.add_roster, name="add roster"),
]