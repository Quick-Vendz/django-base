# nzc urls
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='nzc-home'),
]