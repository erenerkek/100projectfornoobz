def vowelFinder(text,):
    counter = 0
    vowels = "aeiouAEIOU"
    for char in text:
        if char in vowels:
            counter+=1
    return counter

text = input("Enter your Text: ")
print("{} vowels in your text.".format(vowelFinder(text)))

        
