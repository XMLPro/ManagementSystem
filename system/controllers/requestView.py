from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from system.models import *
from django.contrib.auth.decorators import *


@login_required
def requestView(request):
    request_list = Request.objects.all()
    ctxt = RequestContext(request,{
        'request_list': request_list,
    })
    for req in request_list:
        print(req)
    else:
        print("NO data")
    return render_to_response('requestView.html', ctxt)

@login_required
def vote(request):
    try:
        print(request.user.id)
        print(request.POST['request_id'])
        v = Vote(request=request.POST['request_id'], user=request.user.id)
        v.save()
    except:
        print('error')
        raise

    return HttpResponseRedirect(reverse('system:requestView'))
