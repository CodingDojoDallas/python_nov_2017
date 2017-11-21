from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^clear', views.clear),
]