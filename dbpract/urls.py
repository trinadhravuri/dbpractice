from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('pas',views.password,name='password'),
]
