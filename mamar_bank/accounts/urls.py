from django.urls import path

from .views import UserRegistrationView, ProfileView
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('withdraw/', views.withdraw_view, name='withdraw'),
    path('deposit/', views.deposit_view, name='deposit'),
    path('report/', views.report_view, name='report'),
]
