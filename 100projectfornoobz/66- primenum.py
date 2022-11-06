def asal(n):
    for i in range(0,n+1):
        if i%2==0 or i%3==0 or i%5==0 or i%7==0:
            if i==2:
                print("2")
            elif i==3:
                print("3")
            elif i==5:
                print("5")
            elif i==7:
                print("7")
        else:
            if i==1:
                continue
            print(i)
    



n = int(input("Enter your Number: "))

asal(n)


