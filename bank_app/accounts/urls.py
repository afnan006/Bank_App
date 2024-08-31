from django.urls import path
from .views import (
    UserCreateView, BankAccountCreateView,
    TransactionCreateView, TransactionHistoryView,
    LoginLogoutHistoryView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('create-account/', BankAccountCreateView.as_view(), name='create-account'),
    path('transaction/', TransactionCreateView.as_view(), name='transaction'),
    path('transaction-history/', TransactionHistoryView.as_view(), name='transaction-history'),
    path('login-logout-history/', LoginLogoutHistoryView.as_view(), name='login-logout-history'),

    # Authentication endpoints
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
