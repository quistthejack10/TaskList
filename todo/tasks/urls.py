from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='list'),
    path('edit_task/<str:pk>/', views.editTask, name='edit_task'),
    path('delete/<str:pk>/', views.deleteTask, name='delete'),
]
