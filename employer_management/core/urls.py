from django.urls import path
from .views import RegisterView, LoginView, ProfileView, EmployerListCreateView, EmployerRetrieveUpdateDestroyView, APIRootView
from rest_framework_simplejwt.views import TokenRefreshView 

urlpatterns = [
    path('', APIRootView.as_view(), name='api-root'),
    path('auth/signup/', RegisterView.as_view(), name='signup'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/profile/', ProfileView.as_view(), name='profile'),
    path('employers/', EmployerListCreateView.as_view(), name='employer-list-create'),
    path('employers/<int:id>/', EmployerRetrieveUpdateDestroyView.as_view(), name='employer-detail'),
]