# -*- coding:utf-8 -*-
from distutils.version import StrictVersion, LooseVersion

cmp = lambda x, y: StrictVersion(x).__cmp__(y)

assert(StrictVersion('10.4.10') > StrictVersion('10.4.9'))
assert(cmp("10.4.10", "10.4.11") == -1)
assert(not LooseVersion('1.4') > LooseVersion('1.4-rc1'))
assert(LooseVersion('1.4c3') > LooseVersion('1.3'))

assert(LooseVersion('3.0') > LooseVersion('3'))
