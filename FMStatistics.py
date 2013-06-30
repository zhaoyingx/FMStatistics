# -*-coding:utf-8-*-

import urllib2
import cookielib
import urllib
from config import *
import json

def savefile(filename,content):
    file = open(filename,'wb')
    file.write(content)
    file.close

params = {
        "soucre":"radio",
        "alias":EMAIL,
        "form_password":PASSWORD
        }

def login():
    loginurl = LOGINURL
    cookie = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    response = opener.open(loginurl)
    #print response.geturl()
    if response.geturl() == LOGINURL:
        captcha_id = opener.open(urllib2.Request('http://douban.fm/j/new_captcha')).read().strip('"')
        #save captcha-image
        savefile('captcha.jpg',opener.open(urllib2.Request('http://douban.fm/misc/captcha?size=m&id='+captcha_id)).read())
        captcha = raw_input('please input captcha : ')
        print 'waiting for login..'
        response = json.loads(opener.open(
            urllib2.Request('http://douban.fm/j/login'),
            urllib.urlencode({
                'source': 'radio',
                'alias': EMAIL,
                'form_password': PASSWORD,
                'captcha_solution': captcha,
                'captcha_id': captcha_id
                })
            ).read())
        if "err_msg" in response.keys():
            print "login error"
        else:
            print "login success"
    else:
        print "error occur"
    savefile('statistics.html',opener.open(DATAURL).read())

if __name__ == '__main__':
    login()
