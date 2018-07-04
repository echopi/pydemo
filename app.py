# -*- coding:utf-8 -*-

import logging
from logging.handlers import RotatingFileHandler

from flask import request, abort, jsonify
from flask import Flask


app = Flask(__name__)

@app.route('/api/test', methods=['GET', 'POST'])
def test():
  debug = request.args.get('debug')
  return jsonify({
    'debug': debug == 'true'
  })

@app.route('/', methods=['GET'])
def home():
  if request.method == 'POST':
    abort(404)
  return jsonify({
    'home': True
  })

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
