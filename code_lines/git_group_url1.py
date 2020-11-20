#!/usr/bin/python

import requests
import json
quest_ids = ["1", "2", "3", "4", "5"]
duplicated_grpup1 = ["1", "2", "3"]
duplicated_grpup2 = ["4", "5"]
url_edit = "http://192.168.1.204:1234/duplicated-questions/"
url_post = "http://192.168.1.204:1234/duplicated-questions/"
url_delete="http://192.168.1.204:1234/duplicated-questions/"
url_cat = "http://192.168.1.204:1234/duplicated-questions/"
headers = {'content-type': "application/json", "UA": "android8"}
for id in quest_ids:
    url_cat = url_cat + id
    url_delete = url_delete + id
    body = {
        "duplicated_with": [id]
    }
    response_edit = requests.put(url=url_edit, data=json.dumps(body))
    response_post = requests.post(url=url_post, data=json.dumps(body))
    response_delete = requests.delete(url=url_delete)
    response_cat = requests.get(url=url_cat)

    # 获取重复的问题id
    duplicated_ids = response_cat.text["duplicated_with"]

    # 判断返回的id是否在重复组中
    for duplicated_id in duplicated_ids:
        # 问题id在组1 重复id 在组1   返回正常
        if duplicated_id in duplicated_grpup1 and id in duplicated_grpup1:
            print(True)
        # 问题id在组2 重复id在组2   返回正常
        elif duplicated_id in duplicated_grpup2 and id in duplicated_grpup2:
            print(True)
        else:
            # 其他 返回异常
            print(False)