# -*- coding:utf-8 -*-

# https://curl.trillworks.com/
import requests
import json

headers = {
    'accept': 'application/json',
    'content-type': 'application/json',
}

data = {"method":"startTask","network":"3g","clearCache":True,"login":False,"user":{"name":"nobody","job":"cool"},"simulator":True,"configPath":"config/perf-config.js","url":"https://m.douban.com","extraParams":{"reportId":1,"runtime":"lighthouse"}}

response = requests.post('http://127.0.0.1:5000/api/json/test', headers=headers, data=json.dumps(data))


print json.dumps(response.json(), indent=2)
print (response.text, response.ok, response.headers)
