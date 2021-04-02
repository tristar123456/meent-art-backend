from django.urls import path, include
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    path('login', views.Login, name='login'),
    path('logout', views.Logout, name='logout')
]
