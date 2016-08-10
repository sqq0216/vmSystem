import time
from myThread import MyThread

def f():
    try:
        while True:
            time.sleep(0.1)
    finally:
        print "outta here"

if __name__ == "__main__":
    t = MyThread(target=f)
    t.start()
    p = MyThread(target=f)
    p.start()
    print t.isAlive()
    print p.isAlive()
    print t.terminate()
    print t.join()
    print p.isAlive()
    print t.isAlive()
    print p.terminate()
    print p.join()
    print p.isAlive()
    print t.isAlive()
