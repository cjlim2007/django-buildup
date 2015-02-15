from django.conf.urls import patterns, url
urlpatterns = patterns('',
    url(r'^$', 'buildup.views.hello', name='hello'),
    url(r'^time/$', 'buildup.views.time', name='time'),
    url(r'^random/$', 'buildup.views.random', name='random'),
    url(r'^hello/(?P<yourname>\w+)/$', 'buildup.views.hello_template', name='hello_template'),
    url(r'^speak/(?P<sentence>[^/]+)/$', 'buildup.views.speak', name='speak')
)
