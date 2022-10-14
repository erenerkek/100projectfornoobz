
def encrypt(text, value, output=""):
    for char in text:
        output = "{}{}".format(output, chr(ord(char) + value))
    return output

def decrypt(text, value, output=""):
    for char in text:
        output = "{}{}".format(output, chr(ord(char) - value))
    return output

selection = int(input("Welcome to password generator! \n1-Encrypt\n2-Decrypt\nEnter your operation: "))
if selection == 1:
    i = int(input("Enter Your increment level: "))
    text = input("Enter your Text: ")
    print("{}".format(encrypt(text, i)))

elif selection == 2:
    i = int(input("Enter Your increment level: "))
    text = input("Enter your Text: ")
    print("{}".format(decrypt(text, i)))
else:
    print("You selected unavaible operation. o_O")
