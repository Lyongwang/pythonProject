# !/usr/bin/python
# -*- coding: UTF-8 -*-
# 找到第m个只出现n次的字符
# def findTheMcharAndNTimesInString():
#     str = "gbgkkdehh"
#     m = 2
#     n = 1
#     mCount = 0
#     dest = {}  # 存放每个字符出现的次数
#
#     for char in str:
#         if char in dest:
#             dest[char] = dest[char] + 1
#             if dest[char] == n:  # 出现一次 +1
#                 mCount = mCount + 1
#             if mCount == m:  # 判断是否是第m个出现的
#                 print(char)
#                 break
#         else:
#             dest[char] = 1
#             if dest[char] == n:  # 出现一次 +1
#                 mCount = mCount + 1
#             if mCount == m:  # 判断是否是第m个出现的
#                 print(char)
#                 break
#
# if __name__ == "__main__":
#     findTheMcharAndNTimesInString()

# import pandas as pd
# data = [
#
#     {
#       "serviceName": "online-error-uqun-strategy-manage",
#       "slowTime": "5378",
#       "creativeTime": "2/7/2020 17:05:33"
#     },
#     {
#       "serviceName": "online-error-friend-task",
#       "slowTime": "16176",
#       "creativeTime": "2/7/2020 17:30:50"
#     }
# ]
#
# nameList = []
#
# for data1 in data:
#     nameList.append(data1['serviceName'])
#
# result = pd.value_counts(nameList)
# print("result:", result)




