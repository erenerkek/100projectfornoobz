import random
import string

def pasGen():
    n = int(input("How many characters do you want?"))
    password =[]
    
    chars = list(string.ascii_letters+ string.digits + "!'^+%&/()=?")
    random.shuffle(chars)
    for i in range(n):
        password.append(random.choice(chars))
    random.shuffle(password)
    print("".join(password))


    
pasGen()


