from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from system.models import *


def requestView(request):
    request_list = Request.objects.all()
    vote_list = Vote.objects.filter(user=request.user.id)
    ctxt = RequestContext(request, {
        'request_list': request_list,
        'vote_list': vote_list,
    })
    for vote_item in vote_list:
        print(vote_item.request.id)

    for req in request_list:
        print(req.id)
    return render_to_response('requestView.html', ctxt)


def vote(request):
    try:
        print(request.user.id)
        print(request.POST['request_id'])
        request_item = Request.objects.get(pk=request.POST['request_id'])
        request_user = CustomUser.objects.get(pk=request.user.id)
        v = Vote(request=request_item, user=request_user)
        v.save()
    except:
        print('error')
        raise

    return HttpResponseRedirect(reverse('system:requestView'))
