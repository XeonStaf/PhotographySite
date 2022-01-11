from django.contrib import admin
from photoshoots.models import photo_shoot, Album, Review

# Register your models here.
from portfolio.models import Image


admin.site.register(Album)
admin.site.register(Review)