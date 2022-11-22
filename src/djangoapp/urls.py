from django.urls import path
from .views import edit, dashboard, register, contact, contact_sent
from django.urls import reverse_lazy
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetDoneView, PasswordResetView,
                                       PasswordResetCompleteView, PasswordResetConfirmView,
                                       PasswordChangeView, PasswordChangeDoneView,
                                       PasswordResetDoneView,)

app_name = 'djangoapp'

#The template name attributes linkes them to the appropriate HTMl page, each action handles one single aspect.
#reverse_lazy is used for resolving Django URL names into URL paths
urlpatterns = [
    
    
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
    path('dashboard/', dashboard, name='dashboard'),
    path('', LoginView.as_view(template_name='djangoapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='djangoapp/logged_out.html'), name='logout'),
    path('password_change/', PasswordChangeView.as_view(
        template_name='djangoapp/password_change_form.html'), name='password_change'),
    path('password_change/dond/', PasswordChangeDoneView.as_view(template_name='djangoapp/password_change_done.html'),
         name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(
        template_name='djangoapp/password_reset_form.html',
        email_template_name='djangoapp/password_reset_email.html',
        success_url=reverse_lazy('djangoapp:password_reset_done')), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='djangoapp/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='djangoapp/password_reset_confirm.html',
        success_url=reverse_lazy('djangoapp:login')), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='djangoapp/password_reset_complete.html'), name='password_reset_complete'),
    path('contact/', contact, name='contact'), 
    path('contact_sent/', contact_sent, name='contact_sent'), 
            
           
]
