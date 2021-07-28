from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^upload$', views.photo_new, name='UploadPhotos'),
    url(r'^file-upload$', views.Upload, name='upload'),

]