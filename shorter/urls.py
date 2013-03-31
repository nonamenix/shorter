from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView, ListView, DetailView, RedirectView, CreateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from core.models import Short
from core.views import ShortRedirectView, CreateShortView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^add.html', CreateShortView.as_view(model=Short), name="add_short"),
    url(r'^success/(?P<slug>.*)$', DetailView.as_view(slug_field="short_urn",
        model=Short, context_object_name="short"), name='success'),
    url(r'^$', ListView.as_view(model=Short, context_object_name="shorts")),
    url(r'^(?P<short_urn>.*)$', ShortRedirectView.as_view()),


    # Examples:
    # url(r'^$', 'shorter.views.home', name='home'),
    # url(r'^shorter/', include('shorter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:

)
