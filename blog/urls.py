from django.conf.urls import url
from django.contrib import admin
from blog import views
from blog.views import *
from django.conf import settings
from django.conf.urls.static import static
from blog.upload import *
from views import article

urlpatterns = [
    url(r'^$',index, name='index'),
    url(r'^article/$', article, name='article'),
    url(r'^archive/$',archive, name='archive'),
    url(r'^comment/post/$', comment_post, name='comment_post'),
    url(r'^logout$', do_logout, name='logout'),
    url(r'^reg', do_reg, name='reg'),
    url(r'^login', do_login, name='login'),
    url(r'^category/$', category, name='category'),
]
