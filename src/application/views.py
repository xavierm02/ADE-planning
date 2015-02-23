from django import http;
from google.appengine.ext.webapp.template import render
from lxml.html import parse
import urllib2
import os

from google.appengine.api import urlfetch
urlfetch.set_default_fetch_deadline(45)

def string_of_dictionary(dictionary):
    result = ""
    for key, value in dictionary.items():
        result += key + ": " + value + "\n"
    return result
#"https://plannings.univ-rennes1.fr/"
def proxy(request):
    path = request.path
    get = request.GET.copy()
    get['login'] = 'sansesame'
    get['password'] = 'sans2007'
    get['projectId'] = '22'
    get['lang'] = 'en'
    ade_url = 'https://plannings.univ-rennes1.fr' + path + '?' + get.urlencode()
    ade_opener = urllib2.build_opener()
    if 'JSESSIONID' in request.COOKIES:
        ade_opener.addheaders.append(('Cookie', 'JSESSIONID=' + request.COOKIES['JSESSIONID']))
    ade_response = ade_opener.open(ade_url, None, 45)
    response = http.HttpResponse(ade_response.read())
    ade_response_info = ade_response.info()
    if 'set-cookie' in ade_response_info:
        cookie_value = ade_response_info['set-cookie'].split('=')[1].split(';')[0]
        response.set_cookie('JSESSIONID', value=cookie_value)
    return response

def home(request):# request.GET.dict()
    default_url = ''
    result = 'Hello World!'
    template = os.path.join(os.path.dirname(__file__), 'home.html')
    return http.HttpResponse(render(template, {}))
