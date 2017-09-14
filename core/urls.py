from django.conf.urls import include, url
from core.views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    # for our home/index page

    url(r'^register$', register, name='register'),
    # for our register page

    #url(r'^login$', login, name='login'),
    # for our login page

    #url(r'^logout$', logout, name='logout'),
    # for our logout page

    url(r'^short_id/$', redirect_original, name='redirectoriginal'),
    # when short URL is requested it redirects to original URL

    url(r'^makeshort/$', shorten_url, name='shortenurl'),
    # this will create a URL's short id and return the short URL
    ]
