"""
Definition of urls for DjangoWebProject1.
"""

from datetime import datetime
from django.urls import include, re_path, path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from apps import forms, views



urlpatterns = [
    re_path(r'^', include('apps.urls')),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
