import time
from threading import Thread


class A(Thread):
    def run(self):
        for i in range(20):
            if i%2==0:
                print(i)
            time.sleep(1)
class B(Thread):
    def run(self):
        for i in range(20):
            if i%2!=0:
                print(i)
            time.sleep(1)


t1 = A()
t2 = B()
t1.start()
t2.start()