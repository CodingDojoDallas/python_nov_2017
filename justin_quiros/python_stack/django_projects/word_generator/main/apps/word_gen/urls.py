from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.index),
	url(r'^generator$', views.generator),
	url(r'^reset$', views.reset),
	]
 