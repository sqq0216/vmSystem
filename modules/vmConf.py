#!/usr/local/bin/python2.7

#VmConf类负责保存从用户界面读入的虚拟机数据
#vm name
#vm system type
#monitor processes : monitor policy
#monitor port: monitor policy


"""
@author:    chenkuan
@license:   GNU General Public License 2.0
@contact:   chen1511@foxmail.com
@version:   1.0-2016-07-18
"""

class VmConf(object):
    """
    This is the class that save the vm information from the GUI
    """
    def __init__(self):
        self.