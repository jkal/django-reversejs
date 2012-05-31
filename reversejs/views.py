from functools import wraps
from django.http import HttpResponse
from django.core.urlresolvers import get_resolver
from django.utils import simplejson
from urljs.utils import jsonp

def _get_named_patterns():
    """Returns a dictionary with all the named URL patterns."""
    resolver = get_resolver(None)
    patterns = {}
    for key, value in resolver.reverse_dict.iteritems():
        if isinstance(key, basestring):
            patterns[key] = '/%s' % value[0][0][0]
    return patterns

@jsonp
def urljs(request):
    """Hook this into your URLconf to get a JS object of all
    the named URL patterns used in the project. 

    Example:
        url(r'^urljs/$', 'urljs.views.urljs', name='urljs'),
    """
    patterns = _get_named_patterns()
    return HttpResponse(simplejson.dumps(patterns), mimetype='text/javascript')
