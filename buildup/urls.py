from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = patterns('', url(r'^$', 'buildup.views.hello', name='hello'), url(r'^hello_template/(?P<yourname>\w+)/(?P<yoursentence>.+)/$', 'buildup.views.hello_template', name='hello_template'), url(r'^facts/$', 'buildup.views.all_facts', name='all_facts'), url(r'^facts/new/$', 'buildup.views.new_fact', name='new_fact'), url(r'^login/$', 'django.contrib.auth.views.login', name='login'), url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout')) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)