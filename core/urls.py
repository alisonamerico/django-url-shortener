from django.conf.urls import include, url
from core.views import index


urlpatterns = [
    url(r'^$', index, name='index'),
    # for our home/index page

    url(r'^(?P&lt;short_id&gt;\w{6})$', 'redirect_original', name='redirectoriginal'),
    # when short URL is requested it redirects to original URL

    url(r'^makeshort/$', 'shorten_url', name='shortenurl'),
    # this will create a URL's short id and return the short URL
    ]
