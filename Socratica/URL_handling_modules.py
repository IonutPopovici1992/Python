import urllib
from urllib import parse
from urllib import request

"""urllib — URL handling modules"""

"""
    "URL":
    U = Uniform
    R = Resource
    L = Locator
"""

"""
    URL = "https://en.wikipedia.org/wiki/URL?key=value&life=42#History"
    Protocol: http, https, ftp, ...
    Host: en.wikipedia.org
    Port: http = 80, https = 443
    Path: wiki/URL
    Querystring: key=value&life=42
    Fragment: History
"""

"""
    'urllib' is a package that collects several modules for working with URLs:
    1) urllib.request for opening and reading URLs;
    2) urllib.response (used internally);
    3) urllib.error containing the exceptions raised by urllib.request;
    4) urllib.parse for parsing URLs;
    5) urllib.robotparser for parsing robots.txt files.
"""

"""
    HTTP Status Codes:
    200: OK
    400: Bad Request
    403: Forbidden
    404: Not Found
"""

print(dir(urllib))

print(50 * "-")

print(dir(request))

print(50 * "-")

response = request.urlopen("https://www.wikipedia.org")

print(type(response))

print(50 * "-")

print(dir(response))

print(50 * "-")

print(response.code)

print(50 * "-")

print(response.length)

print(50 * "-")

print(response.peek())

print(50 * "-")

data = response.read()
print(type(data))

print(50 * "-")

print(len(data))

html = data.decode("UTF-8")
print(type(html))

print(50 * "-")

print(html)

print(50 * "*")

response2 = request.urlopen("https://www.google.com/search?q=socratica")
data2 = response2.read()
print(data2)

print(50 * "*")

# https://www.youtube.com/watch?v=EuC-yVzHhMI&t=5m56s

qs = "v=" + "EuC-yVzHhMI" + "&" + "t=" + "5m56s"

print(dir(parse))

print(50 * "-")

params = {"v": "EuC-yVzHhMI", "t": "5m56s"}
querystring = parse.urlencode(params)
print(querystring)

print(50 * "-")

url = "https://www.youtube.com/watch" + "?" + querystring
response3 = request.urlopen(url)
print(response3.isclosed())

print(25 * "-")
print(response3.code)

print(25 * "-")

html2 = response3.read().decode("utf-8")
print(html2[:500])
