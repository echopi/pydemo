# -*- coding:utf-8 -*-

import redis

def my_handler(message):
  print message.channel, message.data

r = redis.StrictRedis(host='localhost', port=6379)

p = r.pubsub()

p.subscribe(**{'foo': my_handler })

# while True:
#   message = p.get_message()
#   if message:
#     print message
#   time.sleep(0.001)

thread = p.run_in_thread(sleep_time=0.001)

# thread.stop()
