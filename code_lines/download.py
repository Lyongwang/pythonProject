# !/usr/bin/python
# -*- coding: UTF-8 -*-
import random

url="http://download.app.yiche.com/appchannel/yiche/android/autoeasy_10.42.2_cxxxxxx.apk"
count=1277
group = 13

start = 0
end = 0
jump = 100
for i in range(group):
    end += jump
    print(str(start) + "---" + str(end))
    exam_msg_list = []
    for i in range(start, end):
        exam_msg_list.append(i)
    list = random.sample(exam_msg_list, 10)

    for i in list:
        print(url.replace("xxxxxx", str(i)))
    start += jump
    print("\n")