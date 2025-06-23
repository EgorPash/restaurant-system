from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from users.api_views import ProfileAPIView
from users.views import RegisterView, ProfileView, confirm_user, ProfilePasswordRestoreView, my_cabinet

app_name = "users"

urlpatterns = [
    path("", LoginView.as_view(template_name='users/login.html'), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path('confirm/<str:code>/', confirm_user, name="confirm"),
    path('restore_password/', ProfilePasswordRestoreView.as_view(), name="restore_password"),
    path('my_cabinet/', my_cabinet, name='my_cabinet'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('profile/', ProfileAPIView.as_view(), name='api_profile'),
]