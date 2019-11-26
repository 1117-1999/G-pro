from wsgiref import simple_server , util

def notFound(environ, start_response):
    start_response('404 NotFound',[('Content-type','text/plain')])
    res = '<h1>%s is not found</h1>' % util.request_uri(environ)
    return [res.encode()]

def mainData(environ, start_response):
    start_response('200 Success',[('Content-type','text/html')])
    res = ('<html><head><meta http-equiv="Content-Type" content="test/html"; charset="UTF-8"><title>テスト</title></head><body><h1>テストページ</h1><a href="http://localhost:7000/notfound">適当リンク</a></body></html>'.encode())
    return [res]

application = mainData

if __name__ == '__main__':
    srv = simple_server.make_server('',7000,application)
    print (u':7000で開放')
    srv.serve_forever()