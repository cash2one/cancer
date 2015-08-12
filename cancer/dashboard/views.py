from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.context_processors import csrf
from django.template.defaulttags import register


def index(request):
	args = {}
	args.update(csrf(request))
	args['user'] = request.user
	return render_to_response('consoleView/account.html',args)

######################registered template filters##########################
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def key(d, key_name):
    try:
        value = d[key_name]
    except:
        from django.conf import settings

        value = settings.TEMPLATE_STRING_IF_INVALID

    return value