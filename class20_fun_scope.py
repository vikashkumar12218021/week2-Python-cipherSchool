x = 20
def fun():
     global x
     x=5
     return x

print(x)
print(fun())
print(x)