# !/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import shutil
import sys

group = 'and'

def read_project(project_url, project_branch):
    try:
        root_name = "/Users/lxiansheng/Downloads/temp-project/"+group
        user="liyongwang:lyw.222@"
        project_url = project_url.replace("http://", "http://" + user)
        if not os.path.exists(root_name):
            os.makedirs(root_name)

        root_path = os.path.abspath(root_name)
        os.chdir(root_path)
        split = project_url.split("/")
        project_name = split[len(split) - 1].replace(".git", "")
        project_path = ("%s/%s" % (root_path, project_name))
        clone_result = 0
        if os.path.exists(project_path):
            os.chdir(project_path)
            os.system("git checkout %s" % project_branch)
            if os.system("git pull %s %s" % (project_url, project_branch)) != 0:  # 拉取失败，删除项目并重新克隆
                print("git pull failure, try git clone!")
                os.chdir(root_path)
                clone_result = os.system("git clone -b %s %s" % (project_branch, project_url))
            else:  # 重新克隆
                print("git pull success!")
        else:
            os.chdir(root_path)
            print("git clone first!")
            git_command = "git clone -b %s %s" % (project_branch, project_url)
            clone_result = os.system(git_command)

        if clone_result == 0:
            # cd project/xxx
            os.chdir(project_path)
            return project_name

    except Exception as e:
        print(e)
        # raise e


if __name__ == "__main__":
    count=0
    read_lines = open("git_group_project.txt" + group).readlines()

    for line in read_lines:
        split = line.split("\t")
        print (split[0] + " -- " + split[1])
        project_url = split[0].replace("\n","")
        project_branch = split[1].replace("\n","")
        read_project( project_url, project_branch)
        count=count+1
        print ("remain %s",(len(read_lines) - count))
