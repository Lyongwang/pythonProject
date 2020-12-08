# !/usr/bin/python
# -*- coding: UTF-8 -*-


for i in range(100):
    i = i + 1
    outStr=""
    if i % 3 == 0:
        outStr = outStr + "Fizz"
    if i % 5 == 0:
        outStr = outStr + "Buzz"

    if outStr == "":
        outStr = str(i)

    print(outStr)
