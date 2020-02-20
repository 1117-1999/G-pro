#!/usr/bin/python
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server, WSGIServer
from socketserver import ThreadingMixIn as th

class exWSGIServer(th, WSGIServer):
    pass

def application(environ, start_response):
    url = [a for a in str(environ.get("PATH_INFO")).split(sep="/") if a != ""]
    res = {}
    res["body"] = html["main"]
    res["content"] = "text/html"
    status = "200 OK"
    ContentType = "html"

    if len(url) >= 2:  ContentType = types(url)
    
    try:


        if url[-1] == "favicon.ico":
            with open("./favicon.ico", mode="rb") as f:
                favicon = f.read()
            start_response(status,[("Content-Type","image/vnd.microsoft.icon")])
            return [favicon]
        res = body(url[-1], ContentType)
    except Exception as e:
        print(f"url exception : {e}")        
    start_response(status,[("Content-Type",res["content"])])

    return [res["body"].encode()]

def body(url, content):
    print(f"url:{url}")
    body = html["empty"]
    mime = "text/html"

    if content == "css" and url in css:
        print("request:css")
        body = css[url]
        mime = "text/css"
    elif content == "img" and url in img:
        body = img[url]
        mime = "image/png"
    elif content == "js" and url in js:
        body = js[url]
        mime = "text/javascript"
    elif content == "video" and url in video:
        body = video[url]
        mime = "video/mp4"
    if content == "html" and url in html:
        body = html[url]
        mime = "text/html"
    return {"body":body, "content":mime}

def types(url):
    res_type = ["css","img","js","vodeo"]
    if url[-2] in res_type:
        type_index = res_type.index(url[-2])
        return res_type[type_index]
    else:
        return "html"


if __name__ == "__main__":
    html = {}
    css = {}
    img = {}
    js = {}
    video = {}

    html["main"] = """<!DOCTYPE html>
                <head>
                    <title>main｜</title>
                    <meta charset="utf-8">
                </head>
                <body>
                    <input type="checkbox" id="check">
                    <div class="left_menu">
                        <label for="check">メニュー</label>
                        <ul style="list-style: none;">
                            <li><a href="/selection">ファイルアップロード</a></li>
                            <li>プロフィール</li>
                        </ul>
                    </div>
                    <div class="right_main">
                        <h1>メインページ</h1><hr />
                        <h2>新型コロナウイルスに気を付けましょう</h2>
                    </div>
                    <link rel="stylesheet" type="text/css" href="/css/style">
                </body>"""  

    html["selection"] = """<!DOCTYPE html>
                        <head>
                            <meta charset="utf-8">
                            <title>アップロード｜</title>
                        </head>
                        <body>
                            <input type="checkbox" id="check">
                            <div class="left_menu">                            
                                <label for="check">メニュー</label>
                                <ul style="list-style: none;">
                                    <li><a href="/main">メインページ</a></li>
                                    <li>プロフィール</li>
                                </ul>
                            </div>
                            <div class="right_main">
                                <h1>ファイルアップロード</h1>
                                <div class="content">
                                    <form method="POST" action="/selection" enctype="multipart/form-data" name="main">
                                        <input type="file" name="files" draggable="true"><br />
                                        <input type="submit" value="送信" style="width:80px;">
                                    </form>
                                </div>
                            </div>
                            <link rel="stylesheet" type="text/css" href="/css/style">
                        </body>"""

    html["upload"] = """<!DOCTYPE html>
                    <head>
                        <meta charset="utf-8">
                        <title>アップロード｜</title>
                    </head>
                    <body>
                        <input type="checkbox" id="check">
                            <div class="left_menu">                            
                                <label for="check">メニュー</label>
                                <ul style="list-style: none;">
                                    <li><a href="/main">メインページ</a></li>
                                    <li><a href="/selection">ファイルアップロード</a></li>
                                    <li>プロフィール</li>
                                </ul>
                            </div>
                            <div class="right_main">
                                <h1>{result}</h1>
                                <div class="content">
                                    {filename}のアップロードが{result}しました。<br />
                                    <a href="/selection">ファイル選択に戻る</a><br />
                                    <a href="/list">アップロードしたファイルを確認する</a>
                                </div>
                            </div>
                            <link rel="stylesheet" type="text/css" href="/css/style">
                    </body>"""

    html["empty"] = """<!DOCTYPE html>
                    <head>
                        <meta charset="utf-8">
                        <title>ページが存在しません</title>
                    </head>
                    <body>
                        <script type="text/javascript">
                            alert("ページが存在しません。メインページに移動します")
                            location.replase("/main")
                        </script>
                    </body>"""

    css["style"] = """@charset "utf-8";
                    #check{
                        float: left;
                        margin-top: 15px;
                        height: 10px;
                        padding: 20px;
                        clear: both;
                        padding-bottom: 100vh;
                        margin-right: 10px;
                        margin-bottom: 100vh - 10px;
                        border: 20px double black;
                    }
                    .left_menu{
                        display: none;
                        float: left;
                        height: 100vh;
                    }
                    .right_main{
                        display: block;
                        border-left: transparent 20px solid;
                    }
                    #check:checked ~ .left_menu{
                        display: inline-block;
                        padding: 15px;
                        padding-left: 0px;
                        height: 100vh;
                        border-right: 3px double black;
                        margin-right: 10px;
                    }
                    .content{
                        text-align: center;
                    }
                    ul{
                        padding: 0px;
                    }"""

    try:
        server = make_server(host="", port=8080, app=application, server_class=exWSGIServer)
        print("class:ex")
    except:
        server = make_server(host="", port=8080, app=application)
        print("class:nomal")
    test={}
    test["aaa"] = "Aaa"
    test["abb"] = "Baa"
    print("a" in test)
    print("port:8080 open")
    server.serve_forever()