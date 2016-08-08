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

#import json
try:
    import cPickle as pickle
except ImportError:
    import pickle

import vmState
from vmPolicy import VmPolicy


class VmConf(object):
    """
    This is the class that save the vm information from the GUI
    """
    def __init__(self, name):
        self.clearConf()
        self.__name = name

    def clearConf(self):
        #self.__name = ""
        self.__systype = ""

        self.__checkRootkit = False
        self.__rootkitPolicy = VmPolicy()

        self.__ip = (0,0,0,0)

        self.__processes = []  # 监控进程列表，每个列表项是name,isneed,policy,path
        self.__ports = [] # 监控端口列表，每个列表项是name,isneed,policy


        #self.ssdt = []

    def getConf(self):
        """
        从类对象中获得全部属性
        :return:
        """
        return {"name":self.__name,
                "sysType":self.__systype,
                "isCheckRootkit":self.__checkRootkit,
                "rootkitPolicy":self.__rootkitPolicy.toString(),
                "ip":self.__ip,
                "processesMonitor":self.__processes,
                "portsMonitor":self.__ports}
        #return vars(self)
        #return [var for var in vars(self).values()]

    def setConf(self, kwargs):
        """
        将Conf的各属性存入类对象
        :param kwargs:
        :return:
        """
        self.__systype = kwargs["sysType"]
        self.__checkRootkit = kwargs["isCheckRootkit"]
        self.__rootkitPolicy.setPolicy(kwargs["rootkitPolicy"])
        self.__ip = kwargs["ip"]
        for ps,isneed,policy,path in kwargs['processesMonitor']:
            self.__processes.append((ps,
                                     True if isneed == u"需要" else False,
                                     VmPolicy(policy),
                                     path))
        for pt,isneed,policy in kwargs['portsMonitor']:
            self.__ports.append((pt,
                                 True if isneed == u"需要" else False,
                                 VmPolicy(policy)))

    def getConfFromFile(self):
        """
        # 从文件中读取json数据，读出来是dict
        # 将类对象中所有属性更新
        :return:
        """
        self.clearConf()
        try:
            with open(self.__name + ".vmconf", "r") as f:
                conf = pickle.load(f)
                print conf
                print conf.systype
                print conf.checkRootkit
                print conf.rootkitPolicy
                print conf.rootkitPolicy.level
                print conf.processes
                print conf.ports
                self.__systype = conf.__systype
                self.__checkRootkit = conf.__checkRootkit
                self.__rootkitPolicy = conf.__rootkitPolicy
                self.__processes = conf.__processes
                self.__ports = conf.__ports

        except IOError, e:
            pass

        # try:
        #     with open(self.__name + ".vmconf", "r") as f:
        #         attr_dict = json.load(f)
        #         #将attr_dict中的所有属性分配到当前类中
        #         for key, value in attr_dict:
        #             if hasattr(self, key):
        #                 setattr(self, key, value)
        #             else:
        #                 #类中没有此属性？？？不可能
        #                 pass
        # except IOError, e:
        #     #没有此文件的话不管它，直接清空Conf
        #     pass


    def setConfToFile(self):
        """
        # 将类所有属性序列化到json文件中
        :return:
        """
        with open(self.__name + ".vmconf", "w") as f:
            pickle.dump(self, f)

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

    @property
    def rootkitPolicy(self):
        return self.__rootkitPolicy
    @rootkitPolicy.setter
    def rootkitPolicy(self, rootkitPolicy):
        self.__rootkitPolicy = rootkitPolicy