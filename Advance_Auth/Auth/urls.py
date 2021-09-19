from django.urls import path
from .views import *
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView



urlpatterns=[
    path('home/',Homeview,name='home'),
    path('register/',Registerview,name='register'),
    path('login/',Loginview,name='login'),
    path('logout/',Logoutview,name='logout'),
    path('changepassword/',Changepassview,name='changepass'),
    path('reset_password/',PasswordResetView.as_view(template_name='Auth/reset_password.html'),name='reset_password'),
    path('reset_password_sent/',PasswordResetDoneView.as_view(template_name='Auth/password_reset_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>',PasswordResetConfirmView.as_view(template_name='Auth/password_reset_form.html'),name='password_reset_confirm'),
    path('reset_password_complete/',PasswordResetCompleteView.as_view(template_name='Auth/password_reset_done.html'),name='password_reset_complete'),
]
