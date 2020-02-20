# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server, WSGIServer
from socketserver import ThreadingMixIn as th
import requests
import cgi

class exWSGIServer(th, WSGIServer):
    pass

def application(environ, start_response):
    app_name = select_app(environ.get('PATH_INFO'), 1)
    isApp = call_app(app_name)
    if select_app(environ.get("PATH_INFO"),2) != "home":
        isApp = isApp + "/" + select_app(environ.get("PATH_INFO"),2).encode("iso-8859-1").decode("utf-8")
        print(isApp)
    if environ.get('REQUEST_METHOD') == 'POST':
        wsgi_input = environ['wsgi.input']
        form = cgi.FieldStorage(fp=wsgi_input, environ=environ, keep_blank_values=True, encoding="utf-8")
        res = req_post(isApp, form)
    else:
        res = req_get(isApp)
    start_response('200 OK',[("Content-Type",res[1].get("Content-Type"))])
    return [res[0]]

def call_app(app_name = str):
    print ("app_name : "  + str(app_name))
    if app_name == '': return 'no' 
    app_list = ['home','path', 'method', 'env','file','upload',"list"]
    app = ['home','path_info','request_method','environ', 'file_select','file_upload', 'file_list']

    for i in range(len(app_list)):
        if app_list[i] == app_name :
            print ('app : ' + app[i])
            return (app[i])
    print ("no")
    return 'no'
def req_post(req_url, isData):
    import magic
    print ("req_post")
    data = { 'uploadFile' : (isData["files"].filename, isData.getvalue("files"))}
    #magic.from_buffer(isData.getvalue("files"))
    body = requests.post(url="http://localhost:8000/" + str(req_url), files=data)
    print("req_url1  " + req_url)
    # data = parse.urlencode(data).encode("utf-8")
    # req = request.Request('http://172.16.68.76:8000/' + str(req_url), method='POST')
    # with request.urlopen(url=req, data=data) as res:
        # body = res.read()
    #print (body.content)
    return (body.content, body.headers)
    
def req_get(req_url):
    print ('req_get')
    body = requests.get(url="http://localhost:8000/" + str(req_url))
    print("req_url2  " + req_url)
    # req = request.Request('http://172.16.68.76:8000/' + str(req_url), method='GET')
    # with request.urlopen(url=req) as res:
        # body = res.read()
    return (body.content,body.headers)

def select_app(path, selector):
    isReq = str(path).split(sep='/')
    if len(isReq) > selector:
        return (isReq[selector])
    else:
        return ('home')

if __name__ == '__main__':
    
    try:
        serve = make_server('', 80, application, server_class=exWSGIServer)
    except:
        serve = make_server("", 80, application)
        
    print ("port 80 open")
    serve.serve_forever()