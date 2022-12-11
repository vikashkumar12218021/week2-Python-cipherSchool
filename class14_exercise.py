def greater(a,b):
    if a > b:
        return a
    else:
        return b

n1 =int(input("enter first number: "))
n2 =int(input("enter second number: "))
biggest = greater(n1,n2)
print(f"{biggest} is bigger")