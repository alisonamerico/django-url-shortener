from django.conf.urls import include, url
from core.views import *
from django.contrib.auth import views as auth_views
from core import views as core_views


urlpatterns = [

    url(r'^$', core_views.index, name='index'),
    # for our home/index page
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^search_list/$', SearchList.as_view(), name='search_list'),
    url(r'^(?P<short_id>\w{6})$', redirect_original, name='redirectoriginal'),
    # when short URL is requested it redirects to original URL
    url(r'^makeshort/$', shorten_url, name='shortenurl'),
    # this will create a URL's short id and return the short URL
    ]
