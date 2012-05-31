from functools import wraps

def jsonp(view_func):
    """
    JSONP view decorator.

    Usage:

    @jsonp
    def my_view(request):
        d = {'key': 'value'}
        return HttpResponse(json.dumps(d), content_type='application/json')
    """
    @wraps(view_func)
    def _view(request, *args, **kwargs):
        resp = view_func(request, *args, **kwargs)
        if resp.status_code != 200:
            return resp

        if 'callback' in request.GET:
            callback= request.GET['callback']
            resp['Content-Type']='text/javascript; charset=utf-8'
            resp.content = '%s(%s)' % (callback, resp.content)
            return resp
        elif 'jsonp' in request.GET:
            callback= request.GET['jsonp']
            resp['Content-Type']='text/javascript; charset=utf-8'
            resp.content = '%s(%s)' % (callback, resp.content)
            return resp
        else:
            return resp                

    return _view
