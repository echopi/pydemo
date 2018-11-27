# -*- coding:utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler

from flask import request, abort, jsonify
from flask import Flask
import requests


app = Flask(__name__)

# https://stackoverflow.com/questions/38987/how-to-merge-two-dictionaries-in-a-single-expression
def merge_dict(x, y):
    z = x.copy()   # start with x's keys and values
    z.update(y)    # modifies z with y's keys and values & returns None
    return z

@app.route('/api/test', methods=['GET', 'POST'])
def test():
  debug = request.args.get('debug')
  return jsonify({
    'debug': debug == 'true'
  })

@app.route('/api/json/test', methods=['POST'])
def restful():
  # logger = logging.getLogger(__name__)
  json_dict = request.get_json()

  print json_dict
  if 'login' in json_dict:
    print json_dict['login']
  if 'user' in json_dict:
    print json_dict['user']
  
  result = merge_dict( {
    'x': 1,
    'login': True
  }, json_dict)
  print result
  return jsonify(result);

@app.route('/api/home', methods=['GET'])
def home():
  if request.method == 'POST':
    abort(404)
  return jsonify({
    'home': True
  })

@app.route('/api/wx', methods=['GET'])
def wx():
  appid = request.args.get('appid')
  secret = request.args.get('secret')

  headers = {
    'accept': 'application/json',
    'content-type': 'application/json',
  }
  uri = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (appid, secret)

  response = requests.get(uri, headers=headers)
  if (response.ok):
    return jsonify(response.json())

  return jsonify({
    'msg': 'error'
  })

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
  errorlogHandler = RotatingFileHandler('error.log', maxBytes=100000, backupCount=1)
  errorlogHandler.setLevel(logging.INFO)
  app.logger.addHandler(errorlogHandler)

  accessHandler = RotatingFileHandler('access.log', maxBytes=100000, backupCount=1)
  log = logging.getLogger('werkzeug')
  log.setLevel(logging.INFO)
  log.addHandler(accessHandler)
  
  # logging.basicConfig(filename='error.log',level=logging.DEBUG)
  # logger = logging.getLogger('werkzeug')
  # handler = logging.FileHandler('access.log')
  # logger.addHandler(handler)
  # app.logger.addHandler(handler)

  app.run(host="0.0.0.0", debug=True)
