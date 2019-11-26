from wsgiref import simple_server,util

def notFound(environ, start_response):
    start_response('404 NotFound',[('Content-type','text/plain')])
    res = '%s is not found' % util.request_uri(environ)
    return [res.encode()]

class MiddleWare(object):
    def __init__(self, app):
        self.app = app
    
    def __call__(self, environ, start_response):
        print ("exec middleware")
        return self.app(environ, start_response) 

class WsgiApp(object):
    def __call__(self, environ, start_response):
        print ("middle were")
        start_response('200 OK', [('Content-type', 'text/plain')])
        return [b'hello']

#application = notFound

if __name__ == '__main__':
    application = notFound
    srv = simple_server.make_server('',8000,application)
    print (':8000で開放')
    srv.serve_forever()