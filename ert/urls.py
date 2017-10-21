"""ert URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from blog import views,urls
from blog.views import index,archive
from django.conf import settings
from django.conf.urls.static import static
from blog.upload import *

urlpatterns = [
    # url(r'^uploads/(?P<path>.*)$',  "django.views.static.serve", {"document_root": settings.MEDIA_ROOT,}),
    # static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    url(r'^admin/', admin.site.urls),
    url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
    url(r'^hello/$',views.hello),
    url(r'^', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
