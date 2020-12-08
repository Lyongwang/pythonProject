# !/usr/bin/python
# -*- coding: UTF-8 -*-

import re
def checkMobile(phone):
    if re.match("^1[0-9]{10}$", phone) is not None:
        return True
    else:
        return False

print(checkMobile("28611723412"))