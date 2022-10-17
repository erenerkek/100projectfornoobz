from ast import For


def fibonacci(n):
    f = [0,1]
    for i in range(2,n):
        f.append(f[i-1]+f[i-2])
    for i in range(0,n):
        print(f[i])

print(("*"*30)+"\nWelcome the fibonacci sequence generator!\n"+("*"*30))

n = int(input("n = "))

print(fibonacci(n))