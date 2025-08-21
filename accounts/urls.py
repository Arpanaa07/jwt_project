from django.urls import path, include
from accounts.views import (
    RegisterView,
    LoginView,
    UserProfileAPIView,
    ForgotPasswordView,
    ResetPasswordView
)
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, SupplierViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'suppliers', SupplierViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('api/reset-password/<uidb64>/<token>/', ResetPasswordView.as_view(), name='reset-password'),
    path('profile/', UserProfileAPIView.as_view(), name='user-profile'),
]
