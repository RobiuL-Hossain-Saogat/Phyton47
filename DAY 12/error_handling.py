try:
    list=[10,5,0,30 ]
    result=list[0]/list[5]
    print(result)
except ZeroDivisionError:
    print("Dividing b zero is not possible")
except IndexError:
    print("The number you are using is not available")
finally:
    print("Please check the python manual or visit www.python.org")