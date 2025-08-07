from django.urls import path
from accounts.views import (
    RegisterView,
    LoginView,
    UserProfileAPIView,
    ForgotPasswordView,
    ResetPasswordView
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('api/reset-password/<uidb64>/<token>/', ResetPasswordView.as_view(), name='reset-password'),
    path('profile/', UserProfileAPIView.as_view(), name='user-profile'),
]
