from django.contrib import admin
from photoshoots.models import photo_shoot, Album

# Register your models here.
admin.site.register(photo_shoot)
admin.site.register(Album)