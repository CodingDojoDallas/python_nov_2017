from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
	url(r'^$', views.index),     # This line has changed!
	url(r'^new$', views.new),
	url(r'^(?P<number>\d+)$', views.show),
	# url(r'^$', views.index)
]