from django.urls import path
from . import views

app_name='rostertools'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.RosterListView.as_view(), name='index'),
    path('roster/<int:pk>/', views.RosterDetailView.as_view(), name='view roster'),
    path('users/', views.UserListView.as_view(), name='users'),
    path('user/<str:username>/', views.user_rosters, name='user'),
    # path('roster/mine/', views.my_roster, name='my roster'),
]