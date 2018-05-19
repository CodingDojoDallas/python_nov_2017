from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^users$', views.index, name='index'),
    url(r'^users/new$', views.new, name='new'),
    url(r'^users/(?P<id>\d+)$', views.show),
    url(r'^users/(?P<id>\d+)/edit$', views.edit),
    url(r'^users/(?P<id>\d+)/destroy$', views.destroy),

    url(r'^users/(?P<id>\d+)/update$', views.update),
    url(r'^users/create$', views.create, name='create'),
]