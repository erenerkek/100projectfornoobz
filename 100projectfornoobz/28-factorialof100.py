def factorial(n):
    fac = 1
    if n==0:
        print("Factorial 0 is 1")
    for i in range(1,n+1):
        fac= fac*i
    print(fac)

n = int(input("Enter your value: "))


factorial(n) 