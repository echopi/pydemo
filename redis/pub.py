# -*- coding:utf-8 -*-

import redis
from config import redis_config
import json
r = redis.StrictRedis(**redis_config)


def pub(channel, data):
  r.publish(channel, data)

if __name__ == '__main__':
  pub('foo', json.dumps({
    'user': {
      'name': 'Bob',
      'sex': 'male'
    }
  }))
