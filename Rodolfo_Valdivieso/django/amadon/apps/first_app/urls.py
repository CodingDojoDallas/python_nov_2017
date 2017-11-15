from django.conf.urls import url
from . import views
urlpatterns = [
  url(r'^$', views.index),
  url(r'^goback$', views.goback),
  url(r'^amadon/checkout$', views.checkout),
  url(r'^clearsession$', views.clearsession),
  url(r'^amadon/buy$', views.buy)
]