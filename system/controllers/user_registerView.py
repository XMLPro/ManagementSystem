from django.shortcuts import render_to_response, redirect
from system.models import Equipment, Reserved
from django.template import RequestContext
from django.core.urlresolvers import reverse


def user_register(request):
    return render_to_response("user_register.html", {
        "user": "username",
        })
