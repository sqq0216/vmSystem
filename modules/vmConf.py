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

import logging
logger = logging.getLogger()

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
        self.__systype = u""

        self.__checkRootkit = False
        self.__rootkitPolicy = VmPolicy()

        self.__ip = u'0.0.0.0'

        self.__processes = []  # 监控进程列表，每个列表项是name,isneed,policy,path
        self.__ports = [] # 监控端口列表，每个列表项是name,isneed,policy


        #self.ssdt = []

    def getConf(self):
        """
        # 从类对象中获得全部属性
        :return:
        """
        confdict = {"name":self.__name,
                    "sysType":self.__systype,
                    "isCheckRootkit":self.__checkRootkit,
                    "rootkitPolicy":self.__rootkitPolicy.toString(),
                    "ip":self.__ip}
        # 把processesMonitor属性还原出来
        psMonitor = []
        for ps, isneed, policy, path in self.__processes:
            psMonitor.append((ps,
                             u"需要" if isneed else u"禁止",
                             policy.toString(),
                             path))
        confdict["processesMonitor"] = psMonitor
        # 把portsMonitor属性还原出来
        ptMonitor = []
        for pt, isneed, policy in self.__ports:
            ptMonitor.append((pt,
                              u"需要" if isneed else u"禁止",
                              policy.toString()
                              ))
        confdict["portsMonitor"] = ptMonitor
        # 返回用户界面显示的所有数据
        return confdict

    def setConf(self, kwargs):
        """
        将Conf的各属性存入类对象
        :param kwargs:
        :return:
        """
        self.clearConf()
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

        logger.debug(unicode(self.__name) + u"配置信息保存到VmConf类中")
        logger.debug(u"当前配置:" + self.__unicode__())

    def getConfFromFile(self):
        """
        # 从文件中读取json数据，读出来是dict
        # 将类对象中所有属性更新
        :return:
        """
        #self.clearConf()
        try:
            with open(self.__name + ".vmconf", "r") as f:
                conf = pickle.load(f)
                self.__systype = conf.__systype
                self.__checkRootkit = conf.__checkRootkit
                self.__rootkitPolicy = conf.__rootkitPolicy
                self.__ip = conf.__ip
                self.__processes = conf.__processes
                self.__ports = conf.__ports
                logger.info(u"从配置文件" + unicode(self.__name) + u".vmconf中读取配置")
                logger.debug(u"读取出的配置：" + self.__unicode__())

        except IOError, e:
            logger.warning(u"配置文件" + unicode(self.__name) + u".vmconf不存在")
            self.clearConf()

    def setConfToFile(self):
        """
        # 将类所有属性序列化到json文件中
        :return:
        """
        with open(self.__name + ".vmconf", "w") as f:
            pickle.dump(self, f)
        logger.info(u"虚拟机" + unicode(self.__name) + u"配置信息保存到文件中")

    def __str__(self):
        """
        # 输出类中全部内容
        :return:
        """
        dict  = {u"name":self.__name,
                u"sysType":self.__systype,
                u"isCheckRootkit":self.__checkRootkit,
                u"rootkitPolicy":unicode(self.__rootkitPolicy),
                u"ip":self.__ip,
                u"processesMonitor":[],
                u"portsMonitor":[]}
        for ps,isneed,policy,path in self.__processes:
            dict[u"processesMonitor"].append((ps, isneed, unicode(policy), path))
        for pt,isneed,policy in self.__ports:
            dict[u"portsMonitor"].append((pt, isneed, unicode(policy)))
        return str(dict)

    def __unicode__(self):
        """
        # 以中文可见的方式输出conf内容
        :return:
        """
        return self.__str__().decode("unicode-escape")

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
    def ip(self):
        return self.__ip
    @ip.setter
    def ip(self, ip):
        self.__ip = ip

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