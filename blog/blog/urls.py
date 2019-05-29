from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^article/$', 'articles.views.archive',name='get_articles'),
    url(
        r'^article/(?P<article_id>\d+)$',
        'articles.views.get_article',
        name='get_article'
    ),
    url(r'^article/new/','articles.views.create_post'),
    url(r'^article/newuser/','articles.views.create_puser'),
    url(r'^article/user/','articles.views.create_auto'),
    url(r'^logout/','articles.views.create_logout'),
)
