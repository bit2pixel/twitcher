from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # url(r'^$', 'twitcher.views.home', name='home'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/1', include('twitterapi.urls')),
)
