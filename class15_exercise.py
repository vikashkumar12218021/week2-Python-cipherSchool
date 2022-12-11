def greater(a,b,c):
    if a > b > c or a > c > b:
        return a
    else:
        if b > c > a or b > a > c:
            return b
        else:
            c > a > b or c > b > a
            return c
n1 = int(input("enter first number: "))
n2 = int(input("enter second number: "))
n3 = int(input("enter third number: "))
biggest = greater(n1,n2,n3)
print(f"{biggest} is greater")