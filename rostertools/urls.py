from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('view/<int:roster_id>/', views.view_roster, name='view roster'),
]