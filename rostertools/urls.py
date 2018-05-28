from django.urls import path
from . import views

app_name='rostertools'
urlpatterns = [
    path('', views.index, name='index'),
    path('user/<str:username>/', views.user_rosters, name='user'),
    path('view/<int:roster_id>/', views.view_roster, name='view roster'),
]