from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^amadon$', views.index),
    url(r'^amadon/checkout$', views.checkout),
    url(r'^amadon/process$', views.process)
]