# !/usr/bin/python
# -*- coding: UTF-8 -*-
import logging
import os
import time

import json
import requests

javaFilePath = "./src/main/java/com/github/api/service/"
packageName = "package com.github.api.service;\n\n"
otherImportLine = "import com.bitauto.libcommon.net.model.HttpResult;\n"
responseClass = "HttpResult<Object>"
author = "Lyongwang"
email = "liyongwang@yiche.com"
FILE_TYPE = "MultipartBody.Part"
logFileName = 'error.log'
apiListUrlClass = "AppUrls"
apiServiceClass = "AppService"


# 写文件
def writeToFile(fileName, fileContent):
    if not os.path.exists(javaFilePath):
        os.mkdirs(javaFilePath)
    fileName = javaFilePath + fileName + ".java"
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
    importLines = otherImportLine + \
                  "import retrofit2.http.Multipart;\n" \
                  "import okhttp3.MultipartBody;\n" \
                  "import io.reactivex.Observable;\n" \
                  "import retrofit2.http.Field;\n" \
                  "import retrofit2.http.FormUrlEncoded;\n" \
                  "import retrofit2.http.GET;\n" \
                  "import retrofit2.http.POST;\n" \
                  "import android.support.annotation.NonNull;\n" \
                  "import retrofit2.http.Query;\n\n"
    classNotes = "/**" \
                 "\n * @author " + author + \
                                      "\n * @date " + \
                 time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()) + \
                 "\n * <p>" \
                 "\n * Email: " + email +\
                 "\n */\n"
    # print("classAnnotation ---> \n" + classNotes)
    classLine = "public interface " + apiServiceClass + " {\n"
    # print("classLine ---> " + classLine)
    methodsTexts, urlTexts, urlMapTexts = parseMethods(apiList)
    fileContent = packageName + importLines + classNotes + classLine
    for methodText in methodsTexts:
        fileContent = fileContent + methodText
    fileContent = fileContent + "\n}"
    print("fileContent --> \n" + fileContent)
    return fileContent, urlTexts, urlMapTexts


methodSet = set([])


# 解析excel表中的每一行(每行表示一个方法)
def parseOneMethod(oneMethod):
    apiDomain = ""
    apiCreatetime = ""
    apiUrl = ""
    apiName = ""
    apiDepartment = ""
    apiAuthor = ""
    apiType = ""
    apiVersionName = ""
    apiParamJson = ""
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
    if "version" in oneMethod:
        apiVersionName = oneMethod["version"]
    if "apiParams" in oneMethod:
        apiParamJson = oneMethod["apiParams"]
    methodUrl: str = (apiDomain + apiUrl).replace("http:", "https:")
    if methodUrl == "" or not checkUrlRestfull(methodUrl):
        logging.error(" method url error: " + methodUrl)
        return True, methodUrl, "", "", "", apiType, ""
    methodDesc = apiName + " " + str(apiDepartment) + " " + apiAuthor + " " + str(apiCreatetime)
    methodName = getMethodName(methodUrl, apiVersionName)
    if methodName in methodSet \
            or "-" in methodName \
            or "{" in methodName or "}" in methodName\
            or check_contain_chinese(methodName):
        if methodName in methodSet:
            message = " method name has exits!!!"
        else:
            message = " method name error!!!"
        logging.error(message + " " + methodName + " " + methodUrl)
        return True, methodUrl, methodDesc, methodName, "", apiType, ""
    methodSet.add(methodName)
    methodParams = []
    try:
        if "" != apiParamJson:
            methodParams = json.loads(apiParamJson)
    except:
        logging.error(" param is not json: " + apiParamJson)
        return True, methodUrl, methodDesc, methodName, "", apiType, ""
    apiType = apiType.strip().upper()
    urlMockLine = getUrlWithMock(methodName, methodUrl, oneMethod)
    # print(" methodUrl ---> " + methodUrl)
    return False, methodUrl, methodDesc, methodName, methodParams, apiType, urlMockLine



# 获取方法中带有mock的url地址
def getUrlWithMock(methodName, methodUrl, oneMethod):
    mockUrl = ""
    if "mockUrl" in oneMethod:
        mockUrl = oneMethod["mockUrl"]
    if "" == mockUrl:
        mockUrl = methodUrl
    urlMockLine = "        mockUrl.put(" + str(methodName).upper() + ", \"" + mockUrl + "\");\n"
    return urlMockLine


# 解析所有方法
def parseMethods(apiList):
    methodsTexts = []
    urlTexts = []
    urlMapTexts = []
    for oneMethod in apiList:
        # print("oneMethod --->" + str(oneMethod))
        methodError, methodUrl, methodDesc, methodName, methodParams, apiType, urlMapLine = parseOneMethod(oneMethod)
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

        resClassEnd = ">"
        if responseClass == "":
            resClassEnd = ""
        methodLine = "    Observable<" + responseClass + resClassEnd + " " + methodName + "("
        paramIndex = 0
        paramHasFile = False
        paramError = False
        if isinstance(methodParams, list) and len(methodParams) > 0 \
                and "paramType" in methodParams[0] \
                and "children" in methodParams[0] \
                and (methodParams[0]['paramType'] == 11 # 对象类型解析 其中的children
                     or methodParams[0]['paramType'] == 1):# json类型解析 其中的children
            methodParams = methodParams[0]['children']
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
        methodAnnotation = realType + "(AppUrls." + str(methodName).upper() + ")\n"
        # print("methodAnnotation ---> " + methodAnnotation)

        methodsTexts.append(methodNotes)
        methodsTexts.append(methodAnnotation)
        methodsTexts.append(methodLine)
        urlTexts.append("    static final String " + str(methodName).upper() + " = \"" + methodUrl + "\";\n")
        urlMapTexts.append(urlMapLine)
    return methodsTexts, urlTexts, urlMapTexts


# 获取方法名称
def getMethodName(methodUrl, apiVersionName):
    lastIndex = methodUrl.find("?")
    startIndex = findNSubStr(methodUrl, "/", 3)
    if startIndex < 0:
        startIndex = 0
    if lastIndex < 0:
        lastIndex = len(methodUrl)
    methodName = methodUrl[startIndex + 1: lastIndex] + "_" + apiVersionName
    methodName = methodName.replace("/", "_").replace("-", "_").replace(".", "_")
    # print("methodUrl ---->  " + methodUrl + " " + methodName)
    return methodName


def checkUrlRestfull(url):
    if not (url.startswith("http://") or url.startswith("https://")):
        return False

    if not "/" in url[url.find("://") + 3:]:
        return False
    return True


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


# 解析参数
def isInvdidate(paramName):
    if paramName == "" or "\"" in paramName or is_number(paramName):
        return False
    return True


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
        elif 11 == paramType: #文件
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


# 生成全部服务文件
def genAllServiceFile(fileNames):
    interfaces = ""
    index = 0
    for className in fileNames:
        if index > 0:
            interfaces = interfaces + ", "
        interfaces = interfaces + className
        index = index + 1
    fileDesc = "/**\n* 全部服务\n*/\n"
    fileContent = packageName + fileDesc + "public interface AllService extends " + interfaces + " {}"
    # print("fileContent --> \n" + fileContent)
    writeToFile("AllService", fileContent)


def getApiListFromNet():
    header = {"Content-Type": "application/json;charset=UTF-8",
              "token": "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI3NzkxIn0.RyxgA4PTKxUbb2adORrXWC6kfnhTkdwz75LwvwITH0PehB66ObGL696vd257a9veSf3nPnza0ivWsY96DlGRww",
              "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0cnVlTmFtZSI6IuadjuawuOaXuiIsInN1YiI6ImxpeW9uZ3dhbmciLCJpc3MiOiJvcC11Yy1qd3QiLCJuYW1lIjoibGl5b25nd2FuZyIsImV4cCI6MTYwNTc1MzkwMSwiaWF0IjoxNjA1NjY3NTAxLCJ1c2VySWQiOjc3OTF9.EJfLAtgtiPCncz8DUxkVz_WnI5kDM0VLSn2w-dWe-YY"}
    paramMap = "{\"demanTreeList\":[]}"
    # print("demanTreeIds -->" + paramMap)
    apiUrl = "http://192.168.87.178:8889/Api/getApiListExport"
    res = requests.post(apiUrl, headers=header, data=paramMap)
    resStr = res.text
    print("response ---> " + resStr)
    response = json.loads(resStr)
    if response["status"] != 1:
        raise Exception(print("api error: " + response["msg"]))
    return response["data"]


# 解析文件名
def parseFileName(fileName:str):
    # fileName = fileName[fileName.rfind("_") + 1:fileName.rfind(".")].replace(".", "_").upper()
    # if index > 0:
    #     fileName = fileName + "_" + sheetName
    return "V" + fileName.replace(".", "_")


# 解析接口数据
def writeAppUrlClass(urlTexts, urlMapTexts):
    urlHeaderText = "package com.github.api.service;\n\n" \
                    "import java.util.HashMap;\n" \
                    "import java.util.Map;\n\n"\
                    "/**\n" \
                    " *\n" \
                    " * @author Lyongwang\n" \
                    " * @date " \
                    + time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()) + "\n" \
                    " * <p>\n" \
                    " * Email: " + email + "\n" \
                    " */\n" \
                    "public class "+ apiListUrlClass +" {\n" \
                    "    static Map<String, String> mockUrl = new HashMap<>();\n"
    urlFooterText = "}\n"
    urlContent = ""
    urlMockContent = ""
    for urlText in urlTexts:
        urlContent = urlContent + urlText
    for urlMockText in urlMapTexts:
        urlMockContent = urlMockContent + urlMockText
    classContent = urlHeaderText + urlContent + "    {\n" + urlMockContent + "    }\n" + urlFooterText
    writeToFile(apiListUrlClass, classContent)



# 解析所有数据
def parseData():
    apiList = getApiListFromNet()
    # 解析java类
    fileContent, urlTexts, urlMapTexts = paseJavaClass(apiList)
    # 写文件
    writeToFile(apiServiceClass, fileContent)
    # 写带有mock url切换的类
    writeAppUrlClass(urlTexts, urlMapTexts)

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