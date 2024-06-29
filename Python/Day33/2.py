def fun1():
    print("entering Fun1")
    try:
        fun2()
    except Exception as e:
        print("error in fun1")
        raise e
    finally:
        print("Leaving fun1")
def fun2():
    print("entering Fun2")
    try:
        res = 10/0
        print(res)
    except Exception as e:
        print("error in fun2")
        raise e
    finally:
        print("Leaving fun2")
print("pgm Started")
try:
    fun1()
except Exception as e:
    print("error in main")
print("pgm end")