x=9
y=0
try:
    print("error class open")
    print(x/y)
    t=int(input("enter number"))
    print(t)
    # print(me)
except ZeroDivisionError as e:
    print(" cant divide by 0",e)
except ValueError as e:
    print("was not asked for this")
except Exception as e:
    print("its just wrong")
finally:
    print("error class closed")