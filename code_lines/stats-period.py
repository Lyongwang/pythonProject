# !/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import shutil
import sys


def obtain_line(start_date, end_date):
    # command = """git log  --pretty=tformat: --since ==2020–3-01 --until=2020-5-14 --numstat | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s", add, subs, loc }'"""

    since = ''
    if len(start_date) > 0 and len(end_date) > 0:
        since = "--since ==%s --until=%s" % (start_date, end_date)
    command_a = "git log  --pretty=tformat: %s " % since
    command = command_a + """--numstat | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s", add, subs, loc }'"""
    data = os.popen(command).readline()  # added lines: 3845, removed lines: 646, total lines: 3199
    return data


def read_project():
    # try:
        project_url = sys.argv[1]
        project_id = sys.argv[2]
        project_branch = sys.argv[3]
        start_date = sys.argv[4]
        end_date = sys.argv[5]
        print  start_date
        print  end_date

        # git clone 产物目录
        root_name = "project/%s" % project_id
        print  root_name
        if not os.path.exists(root_name):
            os.makedirs(root_name)

        root_path = os.path.abspath(root_name)
        os.chdir(root_path)
        split = project_url.split("/")
        project_name = split[len(split) - 1].replace(".git", "")
        project_path = ("%s/%s" % (root_path, project_name))

        clone_result = 0
        print("project_path=%s" % project_path)
        if os.path.exists(project_path):
            os.chdir(project_path)
            os.system("git checkout %s" % project_branch)
            if os.system("git pull %s %s" % (project_url, project_branch)) != 0:  # 拉取失败，删除项目并重新克隆
                print("git pull failure, try git clone!")
                shutil.rmtree(project_path)
                os.chdir(root_path)
                clone_result = os.system("git clone -b %s %s " % (project_branch, project_url))
            else:  # 重新克隆
                print("git pull success!")
        else:
            print("git clone first!")
            clone_result = os.system("git clone -b %s %s " % (project_branch, project_url))

        if clone_result == 0:
            # cd project/xxx
            os.chdir(project_path)
            lines = obtain_line(start_date, end_date)
            return lines

    # except Exception as e:
    #     raise e


if __name__ == "__main__":
    print(read_project())
