import wsgiref.simple_server


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    path = environ['PATH_INFO']
    if path == '/CalenBio':
        page = '''<!DOCTYPE html>
            <html>
                <head>
                    <meta charset="UTF-8">
                    <title>Calen's Biography</title>
                </head>
                <body>
                    <h1>Hello! My Name is Calen!</h1>
                    <hr>
                    <h2>Age:</h2>
                    <p>I am 17 years old</p>
                    <hr>
                    <h2>School:</h2>
                    <p>I am a homeschooled Senior in High School</p>
                    <hr>
                    <h2>Hobbies:</h2>
                    <p> I enjoy playing my violin, coding (recently), and reading.<br> I like going outside (when it's not pouring down rain) and love to learn.</p>
                    <hr>
                    <h2>Picture of Me:</h2>
                    <p>Click <a href='/CalenBioPic'>Here</a> to see my Picture</p>
                    <hr>
                </body>
            </html>'''

    if path == '/CalenBioPic':
        page = '''<!DOCTYPE html>
            <html>
                <head>
                    <meta charset="UTF-8">
                    <title>Calen's Biography</title>
                </head>
                <body>
                    <h1>Hello! My Name is Calen!</h1>
                    <hr>
                    <h2>Age:</h2>
                    <p>I am 17 years old</p>
                    <hr>
                    <h2>School:</h2>
                    <p>I am a homeschooled Senior in High School</p>
                    <hr>
                    <h2>Hobbies:</h2>
                    <p> I enjoy playing my violin, coding (recently), and reading.<br> I like going outside (when it's not pouring down rain) and love to learn.</p>
                    <hr>
                    <h2>Picture of Me:</h2>
                    <img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.zGbLSPfbI7iI9a48VbOxmgHaEK%26pid%3DApi&f=1" alt="My Picture">
                    <p>Click <a href='/CalenBioPic2'>Here</a> to see another picture of me</p>
                    <hr>
                </body>
            </html>'''

    if path == '/CalenBioPic2':
        page = '''<!DOCTYPE html>
                <html lang="en">
                    <head>
                        <meta charset="UTF-8">
                        <title>Calen's Biography</title>
                    </head>
                    <body>
                        <h1>Hello! My Name is Calen!</h1>
                        <hr>
                        <h2>Age:</h2>
                        <p>I am 17 years old</p>
                        <hr>
                        <h2>School:</h2>
                        <p>I am a homeschooled Senior in High School</p>
                        <hr>
                        <h2>Hobbies:</h2>
                        <p> I enjoy playing my violin, coding (recently), and reading.<br> I like going outside (when it's not pouring down rain) and love to learn.</p>
                        <hr>
                        <h2>Picture of Me when I'm Reading the Scriptures:</h2>
                        <img src="https://caps.pictures/200/5-emperor-groove-2/full/kronks-new-groove-disneyscreencaps.com-3454.jpg" alt="My Picture" width="800" height="500">
                        <hr>
                    </body>
                </html>'''

    return [page.encode()]


httpd = wsgiref.simple_server.make_server('', 8000, application)
httpd.serve_forever()

