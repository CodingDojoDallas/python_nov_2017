from django.conf.urls import url
from . import views
urlpatterns = [
  url(r'^$', views.index),
  url(r'^process_money$', views.process_money),
  url(r'^reset$', views.reset),
  url(r'^farm$', views.farm), 
  url(r'^cave$', views.cave), 
  url(r'^house$', views.house),
  url(r'^casino$', views.casino)
]