import wsgiref.simple_server
import http.cookies


def application(environ, start_response):
    headers = [('Content-Type', 'text/plain; charset=utf-8'),
               ('Set-Cookie', 'name=Calen'),
               ('Set-Cookie', 'favoriteNumber=16'),
               ('Set-Cookie', 'favoriteColor=blue/green')]

    start_response('200 OK', headers)

    if 'HTTP_COOKIE' in environ:
        cookies = http.cookies.SimpleCookie()
        cookies.load(environ['HTTP_COOKIE'])
        res = ""
        for key in cookies:
            res += (key + ": " + cookies[key].value + "\n")
        return[res.encode()]

httpd = wsgiref.simple_server.make_server('', 8000, application)

print("Serving on port 8000...")

httpd.serve_forever()