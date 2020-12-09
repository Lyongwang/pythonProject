# !/usr/bin/python
# -*- coding: UTF-8 -*-
import time

# 平台接口
from abc import ABCMeta, abstractmethod


class BasePlatform(object):
    _metaclass_ = ABCMeta  # 指定这是一个抽象类

    '''生成文件的路径'''
    @abstractmethod
    def getFilePath(self):
        pass

    '''生成文件的后缀名'''
    @abstractmethod
    def getFileExt(self):
        pass

    '''生成服务类的名称'''
    @abstractmethod
    def getServiceName(self):
        pass

    '''生成Url类的名称'''
    @abstractmethod
    def getUrlClassName(self):
        pass

    '''获取服务类内容 methodTexts 方法每行内容'''
    @abstractmethod
    def getUrlClassContent(self, urlTexts):
        pass

    '''获取服务类内容 methodTexts 方法每行内容'''
    @abstractmethod
    def getServiceClassHeader(self):
        pass




'''android 类'''
class AndPlatform(BasePlatform):

    def getServiceClassHeader(self):
        importLines = self.otherImportLine + \
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
                     "\n * @author " + self.author + \
                     "\n * @date " + \
                     time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()) + \
                     "\n * <p>" \
                     "\n * Email: " + self.email + \
                     "\n */\n"
        classLine = "public interface " + self.serviceClassName + " {\n"
        return self.packageName + importLines + classNotes + classLine

    def getFileExt(self):
        return ".java"

    def getFilePath(self):
        return self.javaFilePath

    def getServiceName(self):
        return self.serviceClassName

    def getUrlClassName(self):
        return self.urlClassName

    def getUrlClassContent(self, urlTexts):
        urlHeaderText = "package com.github.api.service;\n\n" \
                        "/**\n" \
                        " *\n" \
                        " * @author Lyongwang\n" \
                        " * @date " \
                        + time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()) + "\n" \
                        " * <p>\n * Email: " + self.email + "\n */\n" \
                        "public interface " + self.urlClassName + " {\n"
        urlFooterText = "}\n"
        urlContent = ""
        for urlText in urlTexts:
            urlContent = urlContent + urlText
        return urlHeaderText + urlContent + urlFooterText

    def __init__(self, apiVersion):
        self.javaFilePath = "./src/main/java/com/github/api/service/"
        self.packageName = "package com.github.api.service;\n\n"
        self.otherImportLine = "import com.bitauto.libcommon.net.model.HttpResult;\n"
        self.responseClass = "Observable<HttpResult<Object>>"
        self.author = "Lyongwang"
        self.email = "liyongwang@yiche.com"
        self.FILE_TYPE = "MultipartBody.Part"
        self.logFileName = 'error.log'
        self.urlClassName = "AppUrls" + apiVersion.replace(".", "_")
        self.serviceClassName = "AppService" + apiVersion.replace(".", "_")



'''ios平台类'''
class IOSPlatfrom(BasePlatform):
    def getFileExt(self):
        pass

    def getUrlClassName(self):
        pass

    def getUrlClassContent(self, urlTexts):
        pass

    def getServiceClassHeader(self):
        pass

    def getFilePath(self):
        return "IOS"

    def getServiceName(self):
        pass
