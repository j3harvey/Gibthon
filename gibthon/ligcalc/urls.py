from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib import admin
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('ligcalc.views',
	(r'^$', 'ligcalc'),
	(r'^get$', 'get'),
)

