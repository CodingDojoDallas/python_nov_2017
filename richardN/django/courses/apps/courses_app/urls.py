from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^courses/process$', views.process),
    url(r'^results', views.result),
]