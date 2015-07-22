from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', include('morningreg.urls', namespace='reg')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^reg/', include('morningreg.urls', namespace='reg')),
)
