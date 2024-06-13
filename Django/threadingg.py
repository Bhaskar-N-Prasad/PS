
import time
from threading import Thread


class Task1(Thread):
    def run(self):
        names = ["Rama","Sita","Ravana"]
        for i in names:
            print(i)
            time.sleep(1)
class Task2(Thread):
    def run(self):
        for i in range(10):
            print(i)
            time.sleep(2)
class Task3(Thread):
    def run(self):
        a = 10
        b = 20
        z = a + b
        print("Sum",z)
t1 = Task1()
t2 = Task2()
t3 = Task3()
t1.start()
t2.start()
t3.start()
# d.printNames()
# d.printNum()
# d.add()