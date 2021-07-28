from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^choose/(?P<pk>\d+)$', views.PhotoShootsDetail, name='choose'),
    url(r'^like/$', views.LikeAction, name='like-action'),
    url(r'^confirm/$', views.Confirm, name='like-confirm')
]