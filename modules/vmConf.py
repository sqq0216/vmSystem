#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

# VmConf类
# 用户配置的信息


"""
@author:    chenkuan
@license:   GNU General Public License 2.0
@contact:   chen1511@foxmail.com
@version:   1.0-2016-07-18
"""

import json
import vmState
from vmPolicy import VmPolicy

class VmConf(object):
    """
    This is the class that save the vm information from the GUI
    """
    def __init__(self):
        self.clearConf()

    def clearConf(self):
        self.__name = ""
        self.__systype = ""

        self.__checkRootkit = False
        self.__rootkitPolicy = VmPolicy()

        self.__ip = ""

        self.__processes = {}  # 监控级别应放在process属性里, str:int，进程名：处理等级
        self.__ports = {}  # 监控级别应放在port属性里


        #self.ssdt = []

    def getConf(self):
        """
        从类对象中获得全部属性
        :return:
        """
        return [var for var in vars(self).values()]

    def setConf(self, **kwargs):
        """
        将Conf的各属性存入类对象
        :param kwargs:
        :return:
        """

    def getConfFromFile(self):
        """
        # 从文件中读取json数据，读出来是dict
        # 将类对象中所有属性更新
        :return:
        """
        self.clearConf()
        try:
            with open(self.__name + ".json", "r") as f:
                attr_dict = json.load(f)
                #将attr_dict中的所有属性分配到当前类中
                for key, value in attr_dict:
                    if hasattr(self, key):
                        setattr(self, key, value)
                    else:
                        #类中没有此属性？？？不可能
                        pass
        except IOError, e:
            #没有此文件的话不管它，直接清空Conf
            pass


    def setConfToFile(self):
        """
        # 将类所有属性序列化到json文件中
        :return:
        """
        with open(self.__name + ".json", "w") as f:
            json.dump(vars(self), f)

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def systype(self):
        return self.__systype
    @systype.setter
    def systype(self, systype):
        self.__systype = systype

    @property
    def processes(self):
        return self.__processes
    @processes.setter
    def processes(self, processes):
        self.__processes = processes

    @property
    def ports(self):
        return self.__ports
    @ports.setter
    def ports(self, ports):
        self.__ports = ports

    @property
    def checkRootkit(self):
        return self.__checkRootkit
    @checkRootkit.setter
    def checkRootkit(self, checkRootkit):
        self.__checkRootkit = checkRootkit