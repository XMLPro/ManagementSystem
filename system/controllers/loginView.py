from django.shortcuts import render_to_response
from django.template import RequestContext



def login(request):
    context = RequestContext(request,
                             {'request': request,
                              'user': request.user})
    print(request.user.is_authenticated())
    if request.user.is_authenticated():
        # print(request.user.objects.all())
        print(request.user.pk)
    return render_to_response('login.html',
                              context_instance=context)
