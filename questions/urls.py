from django.urls import path
from .views import home, take_quiz

urlpatterns = [
    path('', home, name='home'),
]