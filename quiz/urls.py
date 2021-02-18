"""quiz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import (
    LoginView, 
    LogoutView, 
    PasswordChangeView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'), 
    path('login/', LoginView.as_view(
        redirect_authenticated_user=True, template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),

    path(
        'change-password/',
        PasswordChangeView.as_view(
            template_name='registration/change-password.html',
            success_url = '/'
        ),
        name='change_password'),

    path('password-reset/',
        PasswordResetView.as_view(
            template_name='registration/password-reset/password_reset.html',
            subject_template_name='registration/password-reset/password_reset_subject.txt',
            email_template_name='registration/password-reset/password_reset_email.html',
            success_url='/login/'
        ),
        name='password_reset'),

    path('password-reset/done/',
        PasswordResetDoneView.as_view(
            template_name='registration/password-reset/password_reset_done.html'
        ),
        name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(
            template_name='registration/password-reset/password_reset_confirm.html'
        ),
        name='password_reset_confirm'),

    path('password-reset-complete/',
        PasswordResetCompleteView.as_view(
            template_name='registration/password-reset/password_reset_complete.html'
        ),
        name='password_reset_complete'),
]