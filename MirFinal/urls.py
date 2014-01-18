from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MirFinal.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^indexer$','crawler.views.indexPage'),
    url(r'^ajax/index/$','crawler.views.indexIt'),
    url(r'^ajax/search/$','crawler.views.searchIt'),
    url(r'^search/$','crawler.views.searchPage'),
)
