#!/usr/local/bin/python2.7
# -*- coding: utf-8 -*-

self.subthread_fp = PyDump.initJavaSubthreadFPAddress("subthread", True)


count = 10
        while count > 0:
            print "#######################"
            try:
                time.sleep(0.1)
                time_start = time.clock()
                main_result = self.getEvent(self.first_fp, self.fnames, self.vnames, self.vtypes, self.client)
                sub_result = self.getEvent(self.subthread_fp, self.fnames, self.vnames, self.vtypes, self.client)
                time_end = time.clock()
                print "start, end: ", time_start, ",", time_end
                print "Durning: ", (time_end - time_start) * 1000, "ms"
                count -= 1

            except Exception, e:
                print repr(e)