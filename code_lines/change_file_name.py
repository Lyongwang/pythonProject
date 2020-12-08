# !/usr/bin/python
# -*- coding: UTF-8 -*-


path = "/Users/lxiansheng/Downloads/归档/svgs/"


# def file_name(file_dir,file_type=''):#默认为文件夹下的所有文件
#     lst = []
#     for root, dirs, files in os.walk(file_dir):
#         for file in files:
#             if(file_type == ''):
#                 lst.append(file)
#             else:
#                 if os.path.splitext(file)[1] == str(file_type):#获取指定类型的文件名
#                     lst.append(file)
#     return lst
#
#
#
# files = file_name(path,"svg")
# print("---> " + str(files))
#
# for f in files:
#
#     print("---> " + f)
    #设置旧文件名（就是路径+文件名）
    # oldname= path +' \\'+f
    #设置新文件名：源文件名称前加上数字编号_
    # f_new = str(n+1)+'_'+f
    # newname=path+'\\'+f_new
    #用os模块中的rename方法对文件改名
    # os.rename(oldname,newname)

new_ext = ".svg"
import os
data = os.path.abspath(path)
# print(" -> " + str(len(os.listdir(data))))
for i, f in enumerate(os.listdir(data)):
    src = os.path.join(data, str(i) + new_ext)
    dst = os.path.join(data, ("app_danmu_" + str(i) + new_ext))

    ext = os.path.splitext(f)
    print(src + " --> " + dst)
    os.rename(src, dst)
