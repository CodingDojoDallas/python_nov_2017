from django.conf.urls import url
from . import views
urlpatterns = [
  url(r'^$', views.index),
  url(r'^create$', views.create),
  url(r'^goback$', views.goback),
  url(r'^result$', views.result),
]