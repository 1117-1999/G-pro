# -*- coding:utf-8 -*-

# 環境変数（environ）の確認用 #
from wsgiref import simple_server, util

def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    res_a = str(environ).split(sep=',')
    res_b = '<br />'
    for i in res_a:
        res_b = res_b + i + '<br />'

    return [res_b.encode()]

serve = simple_server.make_server('', 8000, app)
serve.serve_forever()
## ここまで ##

# urlの取得 #
#from wsgiref import simple_server, util
#def application(environ, start_response):
#    start_response('200 OK', [('Content-Type','text/html')])
#    print (environ)
#    res = environ.get('PATH_INFO').split(sep='/')
#    aa = "start : "
#    for i in res:
#        aa = aa + i
#    return [aa.encode()]
#serve = simple_server.make_server('', 8000, application)
#serve.serve_forever()
# ここまで #

#__init__,__call__のテスト#
#class aaa(int):
#    def __init__(self,aaaa):
#        self.aaaa = aaaa 
#        print (aaaa)
#        print ('success')
#    def __call__(self,bbbb):
#        self.aaaa = bbbb + self.aaaa
#        print (self.aaaa)
#        print ('next')
#aa = aaa(1221) #__init__のテスト
#aa(9)  #__call__のテスト
# ここまで #

# アプリケーションリクエスト #
#import urllib.request, urllib.error
#from wsgiref import simple_server, util, validate
#def re(rurl):
#    url = rurl
#    html = urllib.request.Request(url)
#    with urllib.request.urlopen(html) as res:
#        body = res.read()
#    return (body)
#def app(environ,start_response):
#    start_response("200 Success",[("Content-Type","text/html")])   
#    body = re('http://localhost:7000')
#    return [body.decode().encode()]
#application = app
#if __name__ == '__main__':
#    vali_app = validate.validator(application)
#    print("ポート8000で開放")
#    server = simple_server.make_server('',8000,vali_app)
#    server.serve_forever()
# ここまで #

# DB呼び出し #
#import MySQLdb
# ここまで #

# URLマッピング #
#from wsgiref import simple_server,util
#class selectApp(object):
#    def __init__(self,table,notfound=notFound):
#        tmp = sorted(table, key=lambda x:len(x),reverse=True)
#        table = [(x, table[X]) for x in tmp]
#        self.table = table
#        self.notfound = notfound
#    def __call__(self, environ, start_response):
#        name = 'SCRIPT_NAME'
#        info = 'PATH_INFO'
#        scriptname = environ.get(name,'')
#        pathinfo = environ.get(info,'')
#        for p, app in self.table:
#            if p == '' or p == '/' and pathinfo.startswith(p):
#                return app(environ, start_response)
#            if pathinfo == p or pathinfo.startswith(p) and pathinfo[len(p)] == '/':
#                scriptname = scriptname + pathinfo
#                pathinfo = pathinfo[len(p):]
#                environ[name] = scriptname
#                environ[info] = pathinfo
#                return app(environ, start_response)
#        return self.notfound(environ, start_response)
#  こ こ ま で  #

# 不正パス用 #
#from wsgiref import simple_server,util
#def notFound(environ, start_response):
#    start_response('404 NotFound',[('Content-type','text/plain')])
#    res = '%s is not found' % util.request_uri(environ)
#    return [res.encode()]
#
#class Nop(object):
#    def __init__(self,application):
#        self.application = application
#    def __call__(self,environ,start_response):
#        return self.application(environ,start_response)
#application = notFound
#if __name__ == '__main__':
#    application = Nop(application)
#    srv = simple_server.make_server('',8000,application)
#    print (u':8000で開放')
#    srv.serve_forever()
#ここまで#

# 二回目 #
#def application(environ,start_response):
#    start_response('200 OK',[('Content-type','text/plain')])
#    res = 'Hello!'
#    return [res.encode()]
#from wsgiref import simple_server
#if __name__ == '__main__':
#    server = simple_server.make_server('',8000, application)
#    print (u"8000で受付中...")
#    server.serve_forever()
#ここまで#

#　最初　＃
#from wsgiref.simple_server import make_server, demo_app
#httpd = make_server('',8000,demo_app)
#print (u'8000ポートで受付中...')
#httpd.handle_request()
#ここまで#