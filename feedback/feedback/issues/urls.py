from django.conf.urls import patterns, url
from django.contrib.auth.views import login

from .views import (list_issues, add_issue, edit_issue, logout_view,
    issues_details)


urlpatterns = patterns(
    '',
    url(r'^$', list_issues, name='list_issues'),
    url(r'^issue/(?P<issue_id>\d+)$', issues_details,
        name='issue_details'),
    url(r'^issue/edit/(?P<issue_id>\d+)$', edit_issue,
        name='edit_issue'),
    url(r'^add', add_issue, name='add_issue'),
    url(r'^login$', login,
        {'template_name': 'login.html'}, name='login'),
    url(r'^logout$', logout_view, name='logout'),
)