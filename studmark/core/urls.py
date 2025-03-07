from django.urls import path, include

from . import views

urlpatterns = [
    path('redir',views.redir,name='redir'),
    path('',views.index,name='index'),
]