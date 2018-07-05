from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
  url(r'^$', views.index),
  url(r'^courses/register', views.register),
  url(r'^courses/login', views.login),
  url(r'^logout', views.logout),
  url(r'^success', views.success),
]