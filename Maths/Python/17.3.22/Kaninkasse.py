def f(x):
    return 24*x-3*x**2

x=1
a=1
b=2

while a<b:
    a=f(x)
    x=x+0.01
    b=f(x)
x=x-0.01
print("Det storste arialet kassen kan ha, er:", f(x), " Og den tilhorende x verdien:", x)



    

