from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^process$', views.process),
    url(r'^result$', views.result),
    url(r'^$', views.index)
]