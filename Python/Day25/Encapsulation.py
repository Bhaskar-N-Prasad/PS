# class Book:
#     def __init__(self,value):
#         self.__pages = value
#     def setter(self,value):
#         if value > 0:
#             self.__pages = value
#     def getter(self):
#         return self.__pages
# b1 = Book(100)
# print(b1.getter())
# b1.setter(114)
# print(b1.getter())
# b1.setter(-99)
# print(b1.getter())
class Student:
    def __init__(self):
        self.__name = ""
    def getter(self):
        return self.__name
    def setter(self,value):
        self.__name = value
    getset = property(getter, setter)
s1 = Student()
s1.getset = "Rama"
res = s1.getset
print(res)
