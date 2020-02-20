# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server, WSGIServer
from socketserver import ThreadingMixIn
import cgi
from http.cookies import SimpleCookie

class exWSGIServer(ThreadingMixIn ,WSGIServer):
    pass

def application(environ, start_response):
    
    app_name = select_app(environ.get('PATH_INFO'), 1)
    result = exec_app(app_name,environ)
    aa = SimpleCookie()
    aa["aaa"] = "alkjs"
    aa["bbb"] = "aaaa"
    header = "; ".join(aa.output().replace("\r\n","").split(sep="Set-Cookie: "))
    print (header[2:])
    start_response('200 OK', [('Content-Type',result[1]),("Set-Cookie",header[3])])
    if type(result[0]) == str:
        return [result[0].encode()]
    return [result[0]]

def exec_app(app, environ):
    import socket
    ip = socket.gethostbyname(socket.gethostname())
    print(ip)
    mime = 'text/html'
    print (app)
    if app == 'no':
        print('no')
        return('<script type="text/javascript">location.replace("/home/")</script>')
    if app == 'home':
        print ('home')
        return ("<meta charset='UTF-8'>デフォルト",mime)
    if app == 'path_info':
        print ('path')
        return (environ.get('PATH_INFO'),mime)
    if app == 'request_method':
        print ('method')
        return (environ.get('REQUEST_METHOD'),mime)
    if app == 'environ':
        print ('env')
        return (str(environ),mime)
    if app == 'file_select':
        print ('file')
        res = '''<html><meta charset='UTF-8'><body>
            <h1>ファイル選択画面</h1>
            <form method="POST" action="/upload" enctype="multipart/form-data" name="main">
            <input type="file" name="files" draggable="true" style="width:100%;height:200px"><br />
            <input type="submit" value="送信" style="width:80px;">
            </form><br /><a href='/list/'>アップロードファイル一覧</a></body></html>'''
        return (res,mime)
    if app == "file_list":
        import os
        paths = "g:/st/files"
        res = "<head><meta charset='utf-8'></head>"
        if select_app(environ.get("PATH_INFO"),2) != "" :
            import urllib.parse as url
            paths = paths + "/" + select_app(environ.get("PATH_INFO"),2)
            print(environ.get("PATH_INFO"))
            print(os.path.isfile(paths))
            if os.path.isfile(paths) == True:
                mime = "application/octet-stream"
                with open(paths, mode="rb") as f:
                    res = f.read()
        elif os.path.isdir(paths) == True:
            file_list = os.listdir(paths)
            res = res + "<h1>アップロードリスト</h1><ol>"
            for lists in file_list:
                res = res + "<li><a href='/list/{0}' download='{1}'>".format(str(lists),str(lists)) + str(lists) + "</li>"
            res = res + "</ol><br /><a href='/file/'>アップロード画面に戻る</a>"
        return (res,mime)
    if app == 'file_upload' and environ.get('REQUEST_METHOD') == 'POST':
        print ('upload')
        print (environ.get('PATH_INFO'))
        print(environ["CONTENT_TYPE"])
        input = cgi.FieldStorage(fp=environ.get("wsgi.input"), environ=environ, keep_blank_values=True,encoding="utf-8")
        print(input["uploadFile"].filename)
        import os
        file_path = "g:/st/files/{}".format(input["uploadFile"].filename)
        if os.path.exists(file_path) == False:
            with open(file_path,mode='wb') as f:
                f.write(input.getvalue("uploadFile"))
                res = "<meta charset='utf-8'><h1>{0}</h1><p>アップロードが完了しました</p><a href='/list'>確認する</a>".format(input["uploadFile"].filename)
        elif app == "file_upload":
            print("B")
            res = "<meta charset='utf-8'><h1>アップロードエラー</h1><p>同名のファイルが存在します。名前を変更してからアップロードしてください。<br/><br /><a href='http://{}/file'>アップロード画面へ戻る</a></p>"
        return (res, mime)
    elif app == "file_upload":
        print ('upload error')
        return ('<script type="text/javascript">location.replace("/home")</script>',mime)
    return ('error',mime)
    
def select_app(path, selector):
    isReq = str(path).split(sep='/')
    if len(isReq) >= selector + 1:
        # print(isReq[selector].encode("iso-8859-1").decode("utf-8"))
        res = isReq[selector].encode("iso-8859-1").decode("utf-8")
        return (res)
    else:
        return ('')

if __name__ == '__main__':
    
    try:
        serve = make_server('', 8000, application, server_class=exWSGIServer)
        serve.serve_forever()
        print(serve["a"].value)
    except: serve = make_server('', 8000, application)
    print ( 'port 8000 open')
    serve.serve_forever()