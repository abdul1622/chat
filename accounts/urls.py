from django.urls import path
from .views import Signup,LoginView,LogoutView,MessageView

urlpatterns = [
    path('',Signup.as_view()),
    path('signin/',LoginView.as_view()),
    path('logout/',LogoutView.as_view()),
    path('message/',MessageView.as_view())
]