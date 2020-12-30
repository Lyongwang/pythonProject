# !/usr/bin/python
# -*- coding: UTF-8 -*-
import json
import logging
import os
import re
import sys
import requests

from code_lines.basePlatform import AndPlatform
from code_lines.basePlatform import BasePlatform
from code_lines.basePlatform import IOSPlatfrom

android = True#sys.argv[1]
apiVersion = str(10.44)#sys.argv[1]

logFileName = 'error.log'


platForm:BasePlatform = None
if android:
    platForm = AndPlatform(apiVersion)
else:
    platForm = IOSPlatfrom(apiVersion)

print("platform--->" + platForm.getFilePath())

# 生成文件的路径
filePath = platForm.getFilePath()
urlClassName = platForm.getUrlClassName()
serviceClassName = platForm.getServiceName()
fileExt = platForm.getFileExt()


responseClass = "Observable<HttpResult<Object>>"
FILE_TYPE = "MultipartBody.Part"


# 写文件
def writeToFile(fileName, fileContent):
    if not os.path.exists(filePath):
        os.makedirs(filePath)
    fileName = filePath + fileName + fileExt
    if os.path.exists(fileName):
        os.remove(fileName)
    openFile = open(fileName, "w")
    openFile.write(fileContent)
    openFile.close()


# 删除日志文件
def delFile(fileName):
    if os.path.exists("./"+fileName):
        os.remove(fileName)


# 解析json并生成java类
def paseJavaClass(apiList):
    fileContent = platForm.getServiceClassHeader()
    methodsTexts, urlTexts = parseMethods(apiList)
    for methodText in methodsTexts:
        fileContent = fileContent + methodText
    fileContent = fileContent + "\n}"
    print("fileContent --> \n" + fileContent)
    return fileContent, urlTexts


methodSet = set([])


# 解析每一个方法
def parseOneMethod(oneMethod):
    apiDomain = ""
    apiCreatetime = ""
    apiUrl = ""
    apiName = ""
    apiDepartment = ""
    apiAuthor = ""
    apiType = ""
    apiParamJson = ""
    apiDoc = ""
    if "apiDomainName" in oneMethod:
        apiDomain = oneMethod["apiDomainName"]
    if "apiURI" in oneMethod:
        apiUrl = oneMethod["apiURI"]
    if "apiName" in oneMethod:
        apiName = oneMethod["apiName"]
    if "department" in oneMethod:
        apiDepartment = oneMethod["department"]
    if "updator" in oneMethod:
        apiAuthor = oneMethod["updator"]
    if "apiRequestType" in oneMethod:
        apiType = oneMethod["apiRequestType"]
    if "updateTime" in oneMethod:
        apiCreatetime = oneMethod["updateTime"]
    if "apiParams" in oneMethod:
        apiParamJson = oneMethod["apiParams"]
    if "apiDocLink" in oneMethod:
        apiDoc = oneMethod["apiDocLink"]
    methodUrl: str = (apiDomain + apiUrl).replace("http:", "https:")
    if methodUrl == "" or not checkUrlRestfull(methodUrl):
        logging.error(" method url error: " + methodUrl)
        return True, methodUrl, "", "", "", apiType
    methodDesc = apiName + " " + str(apiDepartment) + " " + apiAuthor + " " + str(apiCreatetime) + " " + apiDoc
    methodName = getMethodName(methodUrl)
    if methodName in methodSet \
            or "-" in methodName \
            or "{" in methodName or "}" in methodName\
            or check_contain_chinese(methodName):
        if methodName in methodSet:
            message = " method name has exits!!!"
        else:
            message = " method name error!!!"
        logging.error(message + " " + methodName + " " + methodUrl)
        return True, methodUrl, methodDesc, methodName, "", apiType
    methodSet.add(methodName)
    methodParams = []
    try:
        if "" != apiParamJson:
            methodParams = json.loads(apiParamJson)
    except:
        logging.error(" param is not json: " + str(apiParamJson))
        return True, methodUrl, methodDesc, methodName, "", apiType
    apiType = apiType.strip().upper()
    # print(" methodUrl ---> " + methodUrl)
    return False, methodUrl, methodDesc, methodName, methodParams, apiType


# 解析所有方法
def parseMethods(apiList):
    methodsTexts = []
    urlTexts = []
    for oneMethod in apiList:
        # print("oneMethod --->" + str(oneMethod))
        methodError, methodUrl, methodDesc, methodName, methodParams, apiType = parseOneMethod(oneMethod)
        if methodError:
            continue
        if "GET" == apiType:
            realType = "    @GET"
            annotationName = "@Query"
        elif "POST" == apiType:
            realType = "    @FormUrlEncoded\n    @POST"
            annotationName = "@Field"
        else:
            methodSet.remove(methodName)
            logging.error(" method type error: " + apiType)
            continue
        methodNotes = "    /**" \
                      "\n    * " + methodDesc

        methodLine = "    " + responseClass + " " + methodName + "("
        paramIndex = 0
        paramHasFile = False
        paramError = False
        if not isinstance(methodParams, list):
            logging.error(" method params not a list: " + str(methodParams))
            continue
        paramSet = set([])
        for param in methodParams:
            paramError, paramDesc, paramName, paramRealType, paramNotNull = parseParams(methodUrl, methodName, param, methodParams)
            if paramName in paramSet:
                continue
            paramSet.add(paramName)
            if paramError:
                break
            if paramRealType == FILE_TYPE:
                paramHasFile = True
                annotationName = "@Field"
            if paramIndex > 0:
                methodLine = methodLine + ", "
            methodNotes = methodNotes + "\n    * @param " + paramName + " " + paramRealType + " " + paramDesc
            methodLine = methodLine + annotationName + "(\"" + paramName + "\") " + paramNotNull + " " + paramRealType + " " + paramName
            paramIndex = paramIndex + 1

        if paramError:
            continue

        methodLine = methodLine + ");\n\n"
        methodNotes = methodNotes + "\n    * @return" + \
                      "\n    */\n"

        if paramHasFile:
            realType = "    @Multipart\n    @POST"
        methodAnnotation = realType + "(" + urlClassName + "." + str(methodName).upper() + ")\n"
        # print("methodAnnotation ---> " + methodAnnotation)

        methodsTexts.append(methodNotes)
        methodsTexts.append(methodAnnotation)
        methodsTexts.append(methodLine)
        urlTexts.append("    String " + str(methodName).upper() + " = \"" + methodUrl + "\";\n")
    return methodsTexts, urlTexts


# 获取方法名称
def getMethodName(methodUrl):
    lastIndex = methodUrl.find("?")
    startIndex = findNSubStr(methodUrl, "/", 3)
    if startIndex < 0:
        startIndex = 0
    if lastIndex < 0:
        lastIndex = len(methodUrl)
    methodName = methodUrl[startIndex + 1: lastIndex]
    methodName = methodName.replace("/", "_").replace("-", "_").replace(".", "_")
    # print("methodUrl ---->  " + methodUrl + " " + methodName)
    return methodName


# 检查是否为正常url (以http/https开头 包含path)
def checkUrlRestfull(url):
    if re.match(r'^https?:/{2}\w.+$', url):
        return True
    return False


# 检查方法中是否包含中文
def check_contain_chinese(check_str:str):
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
             return True
    return False

# 子串第i次出现的下标
def findNSubStr(str, substr, i):
    count = 0
    while i > 0:
        index = str.find(substr)
        if index == -1:
            return -1
        else:
            str = str[index + 1:]  # 第一次出现的位置截止后的字符串
            print
            str
            i -= 1
            count = count + index + 1  # 字符串位置数累加
    return count - 1


# 是否是数字
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


# 参数名是否合法
def isInvdidate(paramName):
    if paramName == "" or "\"" in paramName or is_number(paramName):
        return False
    return True


# 解析参数
def parseParams(methodUrl, methodName, param, methodParams):
    paramNotNull = ""
    paramDesc = ""
    notNull = 1
    try:
        paramName = param["paramKey"]
        paramType = param["paramType"]
        if not isInvdidate(paramName):
            logging.error(" method param name error: " + str(param) + " " + methodUrl)
            return True, "", "", "", ""

        if "paramNotNull" in param:
            notNull = param["paramNotNull"]
        if "paramName" in param:
            paramDesc = param["paramName"]
        if 0 == paramType or 5 == paramType: # String
            paramRealType = "String"
        elif 3 == paramType or 4 == paramType: # double
            paramRealType = "double"
        elif 2 == paramType or 12 == paramType or 8 == paramType: # int
            paramRealType = "int"
        elif 6 == paramType:  # boolean
            paramRealType = "boolean"
        elif 9 == paramType: # long
            paramRealType = "Long"
        elif 13 == paramType: # 文件
            paramRealType = FILE_TYPE
        else:
            methodSet.remove(methodName)
            logging.error(" method param error type not support: " + str(param) + " " + methodUrl)
            return True, "", "", "", ""
        if notNull == 0:
            paramNotNull = "@NonNull"
    except:
        methodSet.remove(methodName)
        logging.error(" method param error no paramKey or paramType: " + str(methodParams) + " " + methodUrl)
        return True, "", "", "", ""
    return False, paramDesc, paramName, paramRealType, paramNotNull


# 获取api列表
def getApiListFromNet():
    header = {"Content-Type": "application/json;charset=UTF-8",
              "token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI3NzkxIn0.RyxgA4PTKxUbb2adORrXWC6kfnhTkdwz75LwvwITH0PehB66ObGL696vd257a9veSf3nPnza0ivWsY96DlGRww",
              "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0cnVlTmFtZSI6IuadjuawuOaXuiIsInN1YiI6ImxpeW9uZ3dhbmciLCJpc3MiOiJvcC11Yy1qd3QiLCJuYW1lIjoibGl5b25nd2FuZyIsImV4cCI6MTYwNTc1MzkwMSwiaWF0IjoxNjA1NjY3NTAxLCJ1c2VySWQiOjc3OTF9.EJfLAtgtiPCncz8DUxkVz_WnI5kDM0VLSn2w-dWe-YY"}

    paramMap = '{"projectID":"1", "dyflx":"App", "version":"%s"}' % apiVersion
    apiUrl = "http://10.168.49.152:8889/Api/getApiListExport"
    print("request ---> " + apiUrl + "\n" + str(paramMap))
    res = requests.post(apiUrl, headers=header, data=paramMap)
    resStr = res.text
    print("response ---> " + resStr)
    response = json.loads(resStr)
    if response["status"] != 1:
        raise Exception(print("api error: " + response["msg"]))
    return response["data"]


# 解析所有数据
def parseData():
    apiList = getApiListFromNet()
    # 解析java类
    fileContent, urlTexts = paseJavaClass(apiList)
    # 写url地址的类
    writeToFile(urlClassName, platForm.getUrlClassContent(urlTexts))
    # 写服务类
    writeToFile(serviceClassName, fileContent)

# 删除日志文件
delFile(logFileName)
logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='error.log',
                    filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )

parseData()