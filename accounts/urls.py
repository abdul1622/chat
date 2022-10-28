from django.urls import path
from .views import Signup,LoginView,LogoutView

urlpatterns = [
    path('',Signup.as_view()),
    path('signin',LoginView.as_view()),
    path('logout',LogoutView.as_view())
]