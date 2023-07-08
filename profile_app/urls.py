from django.urls import path
from . import views

urlpatterns = [
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('profile/', views.profile_data, name='profile_data'),
]
