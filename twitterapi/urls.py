from django.conf.urls import url
from django.conf.urls import patterns

urlpatterns = patterns(
    'twitterapi',
    url('timeline/(?P<screen_name>\w{1,15}).json', 'views.timeline', name='timeline'),
)