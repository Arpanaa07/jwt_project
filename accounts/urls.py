from django.urls import path
from accounts.views import (
    RegisterView, LoginView,
    ForgetPasswordAPIView, ResetPasswordAPIView,
    UserProfileAPIView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('forget-password/', ForgetPasswordAPIView.as_view(), name='forget-password'),
    path('reset-password/<int:uid>/<str:token>/', ResetPasswordAPIView.as_view(), name='reset-password'),
    path('profile/', UserProfileAPIView.as_view(), name='user-profile'),
]
