from django.core.urlresolvers import reverse
from django.http import Http404


def reverse_or_404(default_name, name=None):
    try:
        return reverse(name if name else default_name)
    except:
        raise Http404
