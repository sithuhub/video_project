from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api
from videos.api import VideoResource

v1_api = Api(api_name='v1')
v1_api.register(VideoResource())

urlpatterns = patterns('',
    # Examples:
    url(r'^', include('mainsite.urls')),
    url(r'^api/', include(v1_api.urls)),
    url(r'^videos/', include('videos.urls')),
    # url(r'^videosite/', include('videosite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
