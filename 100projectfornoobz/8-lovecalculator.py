name1 = input("Enter first person's name: ")
name2 = input("Enter second person's name: ")
vowels =["a","e","u","i","o"]

love = len(name1) + len(name2)



if len(name1) > len(name2):
    love -= 5
elif name1 and name2 in vowels:
    love += 5
else:
    love += 3

    
love = 10 if love > 10 else round(love, 0)


print("{} and {} score is {} out of 10".format(name1, name2, love))

