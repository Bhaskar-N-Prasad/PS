def fun1():
    print("This is function 1") 
    try:
        fun2()
    except Exception as e:
        print("Error in fun1")
        raise e
    print("Leaving fun1")
def fun2():
    print("Entering fun2")
    try:
        res = 10/0
        print(res)
    except Exception as e:
        print("Error in fun2")
        raise e
    print("Leaving fun2")
print("Entering main")
try:
    fun1()
except Exception as e:
    print("leaving main")
print("pgm end")