from django.urls import path

from . import views

app_name = 'users_app'

urlpatterns = [
    path(
        'add-user/',
        views.UserCreateView.as_view(),
        name='user-register',
    ),
    path(
        'login-user/',
        views.LoginUser.as_view(),
        name='login-register',
    ),
    path(
        'logout/',
        views.LogoutView.as_view(),
        name='user-logout',
    ),
    path(
        'update-password/',
        views.UpdatePasswordView.as_view(),
        name='update-password',
    ),
    path(
        'verification/<pk>/',
        views.CodeVerificationView.as_view(),
        name='verification',
    ),
]