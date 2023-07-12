from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from user.views import (
    CreateUserView,
    ManageUserView,
    LogoutView,
    ListUserView, ManageUserProfileView
)

urlpatterns = [
    path("register/", CreateUserView.as_view(), name="create"),
    path("me/", ManageUserView.as_view(), name="manage"),
    path("me/profile/", ManageUserProfileView.as_view(), name="manage_profile"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("users/", ListUserView.as_view(), name="search"),
]

app_name = "user"
