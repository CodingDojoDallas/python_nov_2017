from django.conf.urls import url
from . import views
urlpatterns = [
  url(r'^$', views.index),
  url(r'^session_word$', views.index),
  url(r'^addWord$', views.addWord),
  url(r'^clearWord$', views.clearWord)

]