def division(a,b):
    try:

        return a/b
    except ZeroDivisionError:
        print('you cannot divide a number by zero')

print(division(10,0))