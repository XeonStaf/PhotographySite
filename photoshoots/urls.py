from django.conf.urls import url
from django.urls import path
from . import views



urlpatterns = [
    url(r'^choose/(?P<pk>\d+)$', views.PhotoShootsDetail, name='choose'),
]