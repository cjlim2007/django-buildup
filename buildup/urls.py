from django.conf.urls import patterns, url
urlpatterns = patterns('',
    url(r'^$', 'buildup.views.hello', name='hello'),
    url(r'^hello_template/(?P<yourname>.+)/$', 'buildup.views.hello_template', name='hello_template')
)
