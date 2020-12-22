# !/usr/bin/python
# -*- coding: UTF-8 -*-

import os

group = 'and'


if __name__ == "__main__":
    count=0
    read_lines = open("git_group_project.txt" + group).readlines()
    root_name = "/Users/lxiansheng/Downloads/temp-project/" + group
    files = os.listdir(root_name)

    for line in read_lines:
        inLine = False
        for file in files:
            if file in line:
                inLine = True
        if not inLine:
            print("not in line:" + line)
        else:
            print("in line:" + line)
