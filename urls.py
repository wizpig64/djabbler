from django.conf.urls.defaults import *
from djabbler.views import hello

urlpatterns = patterns('',    
    (r'^',  hello),
)
