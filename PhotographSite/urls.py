"""PhotographSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from user.views import account_signup_view
from django.conf.urls.static import static
from . import settings
from portfolio.views import index


urlpatterns = [
    path('', index, name='portfolio'),
    path('login/', view=account_signup_view),
    path('accounts/', include('allauth.urls')),
    path('user/', include('user.urls')),
    path('admin/', admin.site.urls),
    path('photoshoots/', include('photoshoots.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('photographer-interface/', include('photographer_interface.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
