import imp
from django.urls import path
from .frontend_views import home_view

urlpatterns = [
    path('',home_view)
]