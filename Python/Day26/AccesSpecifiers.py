class Student:
    def __init__(self):
        self.__name = ""
    def dataAccess(self):
        print("Python")
    def __dataAccess(self):
        print("Program")
    def dataAccess2(self):
        self.__dataAccess()
    def _dataAccess3(self):
        print("Data")

s1 = Student()
s1.dataAccess()
s1._dataAccess3()
s1.dataAccess2()