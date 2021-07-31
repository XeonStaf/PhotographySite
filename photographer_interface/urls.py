from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^upload$', views.photo_new, name='UploadPhotos'),
    url(r'^file-upload$', views.upload, name='upload'),
    url(r'^all-photos$', views.all_photo, name='all-photos'),

]