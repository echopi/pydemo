# -*- coding:utf-8 -*-

# https://docs.python.org/2/library/urlparse.html
from urlparse import urlparse

url = 'alipays://platformapi/startapp?appId=2018030502317859'

o = urlparse(url)

protocals = ['https', 'alipays']

result = False

try:
  result = protocals.index(o.scheme) >= 0 
except:
  pass
# o.scheme == 'alipays'

assert(o.scheme == 'alipays')
assert(result) 
