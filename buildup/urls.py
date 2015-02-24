from django.conf.urls import patterns, url
urlpatterns = patterns('', url(r'^$', 'buildup.views.hello', name='hello'), url(r'^hello_template/(?P<yourname>\w+)/(?P<yoursentence>.+)/$', 'buildup.views.hello_template', name='hello_template'), url(r'^facts/$', 'buildup.views.all_facts', name='all_facts'))
