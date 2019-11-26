
import urllib.request, urllib.error
from wsgiref import simple_server, util, validate
def re(rurl):
    url = rurl
    html = urllib.request.Request(url)
    with urllib.request.urlopen(html) as res:
        body = res.read()
    return (body)
def app(environ,start_response):
    start_response("200 Success",[("Content-Type","text/html")])   
    body = re('http://localhost:7000')
    return [body]
application = app
if __name__ == '__main__':
    vali_app = validate.validator(application)
    print("ポート8000で開放")
    server = simple_server.make_server('',8000,vali_app)
    server.serve_forever()