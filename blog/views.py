from __future__ import unicode_literals
import logging
from django.shortcuts import render
from django.conf import settings

logger = logging.getLogger('blog.views')

# Create your views here.
# test github
#2017/10/03

def hello(request):
    return render(request,'hello.html')

def index(request):
    try:
        file = open('ss.txt','r')
    except Exception as e:
        logger.error(e)
    return render(request, 'index.html', locals())

def global_setting(request):
    return {'SITE_NAME': settings.SITE_NAME,
            'SITE_DESC':settings.SITE_DESC,}
