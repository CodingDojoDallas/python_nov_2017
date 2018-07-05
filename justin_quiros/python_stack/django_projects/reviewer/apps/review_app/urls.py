from django.conf.urls import url
from . import views           # This line is new!

urlpatterns = [
  url(r'^$', views.index),
  url(r'^login$', views.login),
  url(r'^register$', views.register),
  url(r'^books$', views.books),
  url(r'^create', views.create),
  url(r'books/(?P<book_id>\d+)$', views.review),
  url(r'^books/add$', views.add),
  url(r'^books/(?P<book_id>\d+)/add', views.add_review),
  url(r'^user/(?P<user_id>\d+)', views.user),
  url(r'^delete/(?P<review_id>\d+)', views.delete),
  url(r'^logout$', views.logout),
]

