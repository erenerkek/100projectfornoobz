def decimaltobin(num):
    if num>=1:
        decimaltobin(num//2)
    print(num%2,end = "")
if __name__ == '__main__':
    num= int(input("Enter your number: "))
    decimaltobin(num)
