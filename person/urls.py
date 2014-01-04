# -*- coding: utf-8 -*-
from django.conf.urls import *
from bill.views import bill_details

urlpatterns = patterns('person.views',
    url(r'^$', 'membersoverview'),
    url(r'^map$', 'browsemembersbymap', name="person_list"),
	url(r'^(current|all)$', 'searchmembers', name="person_search"),

    url(r'^(?:([A-Za-z]+)(?:/(\d{1,2}))?)?/?$', 'browsemembersbymap'), # Wikipedia has bad links using state names instead of abbrs, so we support it

	url(r'^[^/]+/(\d+)$', 'person_details', name='person_details'), # name slug (but it's ignored) "/" ID
    url(r'^([A-Z]?\d+)$', 'person_details', name='person_details'), # allow bioguide ID here
	url(r'^[^/]+/(\d+)/report-card/(\d{4})', 'person_session_stats', name='person_session_stats'), # name slug "/" ID "/year-end/" session name (year)
	url(r'^export/report-card/(\d{4})/([^/]+)/([^/\.]+).csv', 'person_session_stats_export', name='person_session_stats_export'),
	
    url(r'^ajax/district_lookup$', 'district_lookup'),
	url(r'^embed/mapframe(?:\.xpd)?$', 'districtmapembed', name='districtmapembed'),
)
