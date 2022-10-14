print("Choose your operation:\n 1-Fahrenheit to Celcius\n 2- Celcius to Fahrenheit")
choice = int(input("Enter Your Choice (1/2): "))

if choice== 1:
    fahrenheit = float(input("Degree to  coonvert: "))
    celcius = (fahrenheit - 32)/1.8
    print("{} degree fahrenheit is equal to {} degree celsius.".format(fahrenheit, celcius))
elif choice == 2:
    celcius = float(input("Degree tı convert: "))
    fahrenheit = (celcius*1.8)+32
    print("{} degree celcius is equal to {} degree fahrenheit.".format(celcius, fahrenheit))
else:
    print("Great! You hacked this super complex program.")