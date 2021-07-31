from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^choose/(?P<pk>\d+)$', views.PhotoShootsDetail, name='choose'),
    url(r'^like/$', views.like_action, name='like-action'),
    url(r'^confirm/$', views.confirm, name='like-confirm'),
    url(r'^review/(?P<pk>\d+)$', views.review_new, name='review'),
    url(r'^review/confirm', views.confirm_review, name='review-confirm'),
]