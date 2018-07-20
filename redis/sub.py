# -*- coding:utf-8 -*-

import redis
from config import redis_config

def my_handler(message):
  print message


r = redis.StrictRedis(**redis_config)

p = r.pubsub()

p.subscribe(**{'foo': my_handler })
p.subscribe(**{'lighthouse': my_handler })

# while True:
#   message = p.get_message()
#   if message:
#     print message
#   time.sleep(0.001)

thread = p.run_in_thread(sleep_time=0.001)

# thread.stop()
