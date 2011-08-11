from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

constructpatterns = patterns('gibson.views',
	(r'^$', 'construct'),
	(r'^summary$', 'summary'),
	(r'^settings$', 'settings'),
	(r'^settings/edit$', 'settings_edit'),
	(r'^delete$', 'construct_delete'),
	(r'^view/(?P<fid>\d+)$', 'fragment_viewer'),
	(r'^add$', 'fragment_browse'),
	(r'^add/(?P<fid>\d+)$', 'fragment_add'),
	(r'^delete/(?P<fid>\d+)$', 'fragment_delete'),
	(r'^save$', 'save'),
	(r'^process$', 'process'),
	(r'^primers/$', 'primers'),
	(r'^primers/csv$', 'csv_primers'),
	(r'^primers/(?P<pid>\d+)/', 'primer'),
	(r'^primers/(?P<pid>\d+)$', 'load_primer'),
)

urlpatterns = patterns('gibson.views',
	(r'^$', 'constructs'),
	(r'^add$', 'construct_add'),
	(r'^(?P<cid>\d+)/\w+\.gb', 'download'),
	(r'^(?P<cid>\d+)/[\w\d ]+/', include(constructpatterns)),
)
