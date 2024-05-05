from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('grades/', views.grades_view, name='grades'),
    path('transactions/', views.transactions_view, name='transactions'),
]
