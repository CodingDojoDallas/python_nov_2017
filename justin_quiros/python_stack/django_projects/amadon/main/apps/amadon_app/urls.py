from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
  url(r'^$', views.index),
  url(r'^process$', views.process),
  url(r'^checkout$', views.checkout),
  url(r'^clear$', views.clear),     # This line has changed!
  url(r'^goback$', views.index),     # This line has changed!
       # This line has changed!
]