# a=5
# b=2
# k=int(input("enter a number"))
# print(k)
# try:
#     print("resource open")
#     print(a/b)
# except Exception as e:
#     print("hey, you cannot divide a number by 0",e)
# finally:
#     print("resource closed")


# writing a program different error exceptions
a=5
b=2

try:
    print("resource open")

    print(a/b)
    k = int(input("enter a number"))
    print(k)
except ZeroDivisionError as e:
    print("hey, you cannot divide a number by 0",e)
except ValueError as e:
    print("invalid input")
except Exception as e:
    print("something went wrong")
finally:
    print("resource closed")
