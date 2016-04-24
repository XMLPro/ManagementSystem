from django.shortcuts import render_to_response
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


def notAllowView(request):
    if request.user.is_valid:
        return redirect(reverse("system:top"))
    return render_to_response("notAllowView.html")
