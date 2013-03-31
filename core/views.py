# Create your views here.
from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView
from core.models import Short


class ShortRedirectView(RedirectView):
    # permanent = False
    # query_string = True

    def get_redirect_url(self, **kwargs):
        print kwargs
        short = get_object_or_404(Short, short_urn=kwargs.get('short_urn'))
        short.increase_conversions()

        # short_urn = kwargs['short_urn']
        # print short_urn
        # short = Short.objects.get(short_urn=short_urn)
        # return short.full_uri

        return short.full_uri