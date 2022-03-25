from django.urls import path
from . import views

urlpatterns = [
    path('competition/', views.competition, name='competition'),
    path('quest/', views.quest, name='quest'),
]