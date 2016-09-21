# -*- coding: utf-8 -*-
import unix

ip = '192.168.122.12'
uname = 'root'
passwd = '123456'

h = unix.Remote()
h.connect(ip, username=uname, password=passwd)

while True:
    status, path, _ = h.execute("pwd")
    if not status: break
    cmd = raw_input("["+uname+"@"+uname+" "+path+"]$ ")
    if cmd == "endremote": break
    info = h.execute(cmd)
    if not info[0]:
        print "命令执行失败"
    else:
        print info[1].decode('utf-8')