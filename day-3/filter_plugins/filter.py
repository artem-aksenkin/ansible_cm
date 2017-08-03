from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible import errors
import re

def get_mongo_src(args, os_family, os_ver, mongo_ver):
    result = []
    if os_family == 'RedHat':
        os_family == 'rhel'
    for arg in args:
        count = arg.find(os_family)
        if count != -1:
            count = arg.find(os_ver, count+len(os_family))
            if count != -1:
                count = arg.find(mongo_ver, count+len(os_ver))
                if count != -1:
                    result.append(arg)
    return result

class FilterModule(object):
    def filters(self):
        return {
            'get_mongo_src': get_mongo_src,
        }
