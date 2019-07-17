# -*- coding: utf-8 -*-
import time
import json
import urllib
import requests


def log(str):
    f = open(r'Y:\Users\gaoliang\Desktop\s\log.txt', 'a')
    f.write(str + '\n')
    f.close()

def _encode_params(**kw):
    '''
    do url-encode parameters

    >>> _encode_params(a=1, b='R&D')
    'a=1&b=R%26D'
    >>> _encode_params(a=u'\u4e2d\u6587', b=['A', 'B', 123])
    'a=%E4%B8%AD%E6%96%87&b=A&b=B&b=123'
    '''
    args = []
    for k, v in kw.items():
        if isinstance(v, str):
            qv = v.encode('utf-8')
            v
            args.append('%s=%s' % (k, urllib.request.quote(qv)))
        elif isinstance(v, collections.Iterable):
            for i in v:
                qv = i.encode('utf-8')
                str(i)
                args.append('%s=%s' % (k, urllib.request.quote(qv)))
        else:
            qv = str(v)
            args.append('%s=%s' % (k, urllib.request.quote(qv)))
    return '&'.join(args)
    

def get_auth_url(client_id, redirect_uri):
    return '%s%s?%s' % ('https://api.weibo.com/oauth2/', 'authorize',
                            _encode_params(client_id=client_id,
                                           response_type='code',
                                           redirect_uri=redirect_uri))
                                           
def get_access_token(app_key, app_secret, redirect_url):
    url_auth = get_auth_url(app_key, redirect_url)
    print('[get_access_token]' + url_auth)
    log('[get_access_token]' + url_auth)
    
    code = input('Input code:')
    url_get_token = "https://api.weibo.com/oauth2/access_token"

    payload = {
    "client_id":app_key,
    "client_secret":app_secret,
    "grant_type":"authorization_code",
    "code":code,
    "redirect_uri":redirect_url
    }
    
    res = requests.post(url_get_token, data=payload)
    print(res.text)
    
    resj = json.loads(res.text)
    log('[get_access_token]' + 'access_token = ' + resj['access_token'])
    log('[get_access_token]' + 'remind_in = ' + resj['remind_in'])
    
    return resj['access_token']

def share_weibo(text, img):
    app_key = '1232039546'
    app_secret = 'b81cc8bb4d37b8009d36cbb28fdd7ed1'
    redirect_url = 'https://weibo.com/5296864682/profile?topnav=1&wvr=6'
    
    #access_token = get_access_token(app_key, app_secret, redirect_url)
    access_token = '2.001TGTmFalV42B73c8930ca3SHcoIE'
    
    #安全域名，sina限制文本内容必须有此字段
    safe_domain = 'https://weibo.com/5296864682/profile?topnav=1&wvr=6'
    url_share = 'https://api.weibo.com/2/statuses/share.json'
    
    payload = {
        'access_token':access_token,
        'status':text + ' ' + safe_domain
    }
    if img :
        files = {
            "pic":img
        }
        res = requests.post(url_share, data = payload, files = files)
    else :
        res = requests.post(url_share, data = payload)
        
    log('[share_weibo] ' + text)
    return res

if __name__ == '__main__':
    f = open(r"Y:\Users\gaoliang\Desktop\ziliao\share.jpg", "rb")
    
    text = input('Input text:')
    res = share_weibo(text, f)
    f.close()
    print(res)