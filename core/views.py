# Create your views here.
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import RedirectView, CreateView
from core.models import Short

class CreateShortView(CreateView):
    model = Short
    def get_success_url(self):
        return reverse('success', kwargs = {'slug':self.request.POST['short_urn']})

class ShortRedirectView(RedirectView):
    def get_redirect_url(self, **kwargs):
        short = get_object_or_404(Short, short_urn=kwargs.get('short_urn'))
        short.increase_conversions()
        return short.full_uri


