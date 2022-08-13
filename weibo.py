import requests
import json
import re


class WeiboClient(object):
    def __init__(self, access_token):
        self.access_token = access_token
        self.url = 'https://api.weibo.com/2/'
        self.post_url = self.url + 'statuses/upload_url_text/biz.json'

    def post(self, status, pic=None):
        data = {'status': status}
        files = None
        params = {'access_token': self.access_token}
        if pic is not None:
            try:
                if re.match(r'^https?:/{2}\w.+$', pic):
                    with open('./tmp/pic.png', 'wb') as f:
                        f.write(requests.get(pic, timeout=10).content)
                    pic = './tmp/pic.png'
                files = {'pic': ('pic', open(pic, 'rb'))}
            except Exception as e:
                files = None
        return json.loads(requests.post(self.post_url, data=data, files=files, params=params, is_longtext=1, rip='67.220.91.30').text)
