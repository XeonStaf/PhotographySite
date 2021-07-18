from django.contrib import admin

# Register your models here.
from .models import Image, Categories

admin.site.register(Image)
admin.site.register(Categories)