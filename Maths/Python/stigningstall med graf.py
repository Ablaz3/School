def f(x):
    return 3*x**3-3*x**2+1

delta_x = float(input("Hva er delta X?"))
x = float(input("Hvilken verdi av X vill du regne ut den deriverte for?"))



print("A      derivert")

for x in range (1, 6):
    derivert = (f(x+delta_x)-f(x))/delta_x
    print(f'{a}   {derivert:.2f}')
    a = a+1
