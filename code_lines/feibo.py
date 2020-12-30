# !/usr/bin/python
# -*- coding: UTF-8 -*-

# 1 1 2 3 5 8 13 ... 计算第40个数是多少

first = 1
second = 1


def feiBo(count: int):
    if count == 1 or count == 2:
        return 1
    else :
        return feiBo(count - 1) + feiBo(count - 2)

print(str(feiBo(1)) + " - " + str(feiBo(2))+ " - " + str(feiBo(3))
      + " - " + str(feiBo(4))+ " - " + str(feiBo(5))
      + " - " + str(feiBo(6)) + " - " + str(feiBo(7))
      + " - " + str(feiBo(8)) + " - " + str(feiBo(9)))
print(feiBo(40))