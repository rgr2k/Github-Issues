from django.conf.urls import patterns, url
from django.contrib.auth.views import login

from .views import list_issues, add_issue, logout_view


urlpatterns = patterns(
    '',
    url(r'^$', list_issues, name='list_issues'),
    url(r'^add', add_issue, name='add_issue'),
    url(r'^login$', login,
        {'template_name': 'login.html'}, name='login'),
    url(r'^logout$', logout_view, name='logout'),
)