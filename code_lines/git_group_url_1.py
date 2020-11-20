#!/usr/bin/python
import requests
import sys
import time

url = "http://gitlab.bitautotech.com/api/v4/groups/2554/projects?private_token=S2inDpo1mCg-sf3FZaSb&per_page=100&page=%d"

startTimeStr = "2020-07-01"
endTimeStr = "2020-08-01"

def needWrite(updateTimeStr, createTimeStr):
    # 2020-08-03T17:45:37.000+08:00
    updateTimeStr = updateTimeStr[0:18]
    createTimeStr = createTimeStr[0:18]
    # print timeStr
    updateTimeArray = time.strptime(updateTimeStr, "%Y-%m-%dT%H:%M:%S")
    updateTimestamp = time.mktime(updateTimeArray)
    # print timestamp
    startTimeArray = time.strptime(startTimeStr, "%Y-%m-%d")
    startTimeTamp = time.mktime(startTimeArray)

    endTimeArray = time.strptime(endTimeStr, "%Y-%m-%d")
    endTimeTamp = time.mktime(endTimeArray)

    createTimeArray = time.strptime(createTimeStr, "%Y-%m-%dT%H:%M:%S")
    createTimeTamp = time.mktime(createTimeArray)
    # print finalTimeTamp
    # print timestamp >= finalTimeTamp
    return updateTimestamp >= startTimeTamp and createTimeTamp < endTimeTamp


def get_project_list(index, file):
    print(url % index)
    response = requests.get(url % index)
    project_list = response.json()
    for project in project_list:
        # print(index)
        if needWrite(project['last_activity_at'], project['created_at']):
            writeToFile(file, project)
        pass
    if len(project_list) == 100:
        get_project_list(index + 1, file)


def writeToFile(file, project):
    print "write to file" + str(project['description'])
    file.write(project['http_url_to_repo'] + '#' +
               # (str(project['description']).replace("\n", "").replace("\r", "")) + '#' +
               # project['web_url'] + '#' +
               # (str(project['default_branch'])) + '#' +
               # project['last_activity_at'] + '#' +
               # (str(project['name']).replace("\n", "").replace("\r", ""))) + '#' +
               (str(project['default_branch']).replace("\n", "").replace("\r", "")))

    file.write("\n")


if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding('utf8')
    txtName = "git_group_project.txt"
    f = open(txtName, "a+")
    get_project_list(1, f)
    f.close()
    # get_project_commit()
